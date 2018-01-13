from flask import Flask
from __init__ import app
from flask import session
from flask import url_for
from flask import request

username = None
app.secret_key = "Hello World"


@app.route("/")
def home():
    if username in session:
        return """
        <html>
        <body>
        <h1>You are currently logged in</h1><br />
        <a href='"""+url_for("logoff")+"""'>Log off page</a>
        </body></html>
        """

    else:
        return """
                <html>
                <body>
                <h1>You are currently not logged in</h1><br />
                <a href='""" + url_for("login") + """'>Log in page</a>
                </body></html>
                """

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return """
                        <html>
                        <body>
                        <form method='post'>
                        <input type='text' name='username'/><br />
                        <input type='submit' value='submit' />
                        </form>
                        </body></html>
                        """
    elif request.method == 'POST':

        global username
        username = request.form['username']

        session[username] = username
        return """
            <hrml> <body>
            <a href='""" + url_for("home") + """'>content</a>
            </body></html>
        """

@app.route("/logoff",methods=["GET","POST"])
def logoff():
    if request.method == "GET":
        global username
        if username in session:
            session.pop(username,None)
            username = None
            return """
                    <hrml> <body>
                    <h2>Successfully logged out</h2>
                    <a href='""" + url_for("home") + """'>content</a>
                    </body></html>
                """
        else:
            return """
                                <hrml> <body>
                                <h2>You are not logged in</h2>
                                <a href='""" + url_for("home") + """'>content</a>
                                </body></html>
                            """






