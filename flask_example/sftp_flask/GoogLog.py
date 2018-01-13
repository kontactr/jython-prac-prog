from flask import Flask, redirect, url_for, session, request, jsonify
from flask_oauthlib.client import OAuth
from __init__ import app


app.config['GOOGLE_ID'] = "129383040303-t8g1oblarcla1np4uf85t8ofubod81vv.apps.googleusercontent.com"
app.config['GOOGLE_SECRET'] = "Qj9U7GXAfzR6uUCt04naMSw9 "
app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)

google = oauth.remote_app(
    'google',
    consumer_key=app.config.get('GOOGLE_ID'),
    consumer_secret=app.config.get('GOOGLE_SECRET'),
    request_token_params={
        'scope': 'email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)


@app.route('/log_google',methods=["GET"])
def log_google():
    if "GET" == request.method:
        if 'google_token' in session:
            me = google.get('userinfo')
            #return jsonify({"data": me.data})
            goog_data = me.data

            email, name = "", ""
            if goog_data['email']:
                email = goog_data['email']
            if goog_data['name']:
                name = goog_data['name']
            data = name+"[]"+email+"[]"+goog_data['id']
            session[request.environ['REMOTE_ADDR'] + 'goog_session'] = "true"
            return redirect(url_for('goog_settings', data_obj=data))
        return redirect(url_for('check_google'))


@app.route('/check_google')
def check_google():

    return google.authorize(callback=url_for('authorized', _external=True))


@app.route('/logout_google')
def logout_google():
    session.pop('google_token', None)
    return redirect(url_for('logout'))


@app.route('/check_google/authorized')
def authorized():

    resp = google.authorized_response()

    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (resp['access_token'], '')
    me = google.get('userinfo')
    #return jsonify({"data": me.data})
    return redirect(url_for('log_google'))


@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')
