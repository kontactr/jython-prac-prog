import os
import sqlite3
from datetime import datetime
import redis
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import g
from __init__ import app

DATABASE = "users_data"


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# ------------------------------------------
# database - users
# username - email  -d                      |
# username - password  -d
# username  - friends -d
# username  - requ       -d |
# message:-                                |
# user table:-                             |
# sender - message - time                 |
# ------------------------------------------


# username_session = None
# code = None
user_pass = redis.StrictRedis(db=5, charset="utf-8", decode_responses=True)
user_email = redis.StrictRedis(db=6, charset="utf-8", decode_responses=True)
user_friends = redis.StrictRedis(db=7, charset="utf-8", decode_responses=True)
user_req = redis.StrictRedis(db=8, charset="utf-8", decode_responses=True)


@app.route("/", methods=["GET"])
def home():
    if request.environ['REMOTE_ADDR'] + 'username' not in session:
        return """<html>
        <body>
            <a href='""" + url_for("login") + """'>Login Page</a>
        </body>
        </html>"""
    else:

        return render_template("Dashboard.html", name=session[request.environ['REMOTE_ADDR'] + 'username'])


@app.route("/login", methods=["GET", "POST"])
def login():
    # global username_session
    if request.environ['REMOTE_ADDR'] + 'username' not in session:
        if "GET" == request.method:
            return render_template("Login.html")

        elif request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            if password == user_pass.get(username):
                session[request.environ['REMOTE_ADDR'] + 'username'] = username
                # username_session = username
                return render_template("Dashboard.html", name=session[request.environ['REMOTE_ADDR'] + 'username'])
            else:
                return render_template("Login.html")
    else:
        return render_template("Dashboard.html", name=session[request.environ['REMOTE_ADDR'] + 'username'])


def validation(**kwargs: object) -> bool:
    for key in kwargs:
        if kwargs[key] is None:
            return False
    return True


def code_generate():
    import random as r
    return r.randint(100000, 999999)


def send_mail(email):
    import smtplib as se
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    s = se.SMTP_SSL('smtp.gmail.com')
    msg = MIMEMultipart('alternative')
    msg['Form'] = "ch.email.456@gmail.com"
    msg['To'] = email
    msg['Subject'] = "Activation Code"
    # global code
    session[request.environ['REMOTE_ADDR'] + '_' + 'code'] = str(code_generate())
    msg_part = MIMEText("Activation Code - " + session[request.environ['REMOTE_ADDR'] + '_' + 'code'])
    msg.attach(msg_part)
    s.login("ch.email.456@gmail.com", "ch1234567890")
    s.sendmail("ch.email.456@gmail.com", email, msg.as_string())
    s.quit()


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.environ['REMOTE_ADDR'] + 'username' not in session:
        if request.method == "GET":
            return render_template("Register.html")
        elif request.method == "POST":
            email = request.form["email"]
            username = request.form["username"]
            password = request.form["password"]
            if validation(email=email, username=username, password=password):
                try:
                    if user_pass.exists(username):
                        return "<h1>Username is already taken.</h1><br/>" + render_template("Register.html")
                    else:
                        send_mail(email)
                        session[request.environ['REMOTE_ADDR'] + 'temp_session_user'] = username
                        session[request.environ['REMOTE_ADDR'] + 'temp_session_password'] = password
                        session[request.environ['REMOTE_ADDR'] + 'temp_session_email'] = email
                except Exception as e:
                    if request.environ['REMOTE_ADDR'] + 'temp_session_user' in session:
                        session.pop(request.environ['REMOTE_ADDR'] + 'temp_session_user')
                    if request.environ['REMOTE_ADDR'] + 'temp_session_password' in session:
                        session.pop(request.environ['REMOTE_ADDR'] + 'temp_session_password')
                    if request.environ['REMOTE_ADDR'] + 'temp_session_email' in session:
                        session.pop(request.environ['REMOTE_ADDR'] + 'temp_session_email')
                    return "Sorry InternalError" + render_template("Register.html")

                return """
                <html><body><div>
                <a href='""" + url_for("next_step") + """'>Validate Code</a>
                    </div></body></html>
                """
            else:
                return render_template("Register.html")
        else:
            return render_template("Register.html")
    else:
        return render_template("Dashboard.html", name=session[request.environ['REMOTE_ADDR'] + 'username'])


@app.route("/register/validate", methods=["GET", "POST"])
def next_step():
    # users_msg = sqlite3.connect("users_data", check_same_thread=False,timeout=10.0)
    if request.environ['REMOTE_ADDR'] + 'username' in session:
        return render_template("Dashboard.html", name=session[request.environ['REMOTE_ADDR'] + 'username'])
    else:
        if request.method == "GET":
            if request.environ['REMOTE_ADDR'] + '_' + 'code' in session:
                return """
                <html><body>
                <form method='POST'><div>
                <label id="Code: ">Enter Your Code</label>
                <input type="text" name="code"/><br />
                <input type="submit" value="submit" /><br />
                <input type="submit" value="Resend Code" formaction='""" + url_for('register') + """'
                formmethod="get">
                </div></form></body></html>
                """
            else:
                return render_template("Register.html")
        elif "POST" == request.method:
            if request.environ['REMOTE_ADDR'] + '_' + 'code' in session:
                if session[request.environ['REMOTE_ADDR'] + '_' + 'code'] == request.form["code"]:
                    session.pop(request.environ['REMOTE_ADDR'] + '_' + 'code')
                    user_pass.set(session[request.environ['REMOTE_ADDR'] + 'temp_session_user'],
                                  session[request.environ['REMOTE_ADDR'] + 'temp_session_password'])
                    user_email.set(session[request.environ['REMOTE_ADDR'] + 'temp_session_user'],
                                   session[request.environ['REMOTE_ADDR'] + 'temp_session_email'],
                                   )
                    session.pop(request.environ['REMOTE_ADDR'] + 'temp_session_password')
                    #                    os.mkdir("Data\\"+session[request.environ['REMOTE_ADDR']+'temp_session_user'])
                    user_friends.set(session[request.environ['REMOTE_ADDR'] + 'temp_session_user'], "")
                    user_req.set(session[request.environ['REMOTE_ADDR'] + 'temp_session_user'], "")
                    get_conn = get_db()
                    get_cur = get_conn.cursor()
                    get_cur.execute("CREATE TABLE " + session[request.environ[
                                                                  'REMOTE_ADDR'] + 'temp_session_user'] + "(message "
                                                                                                          "text, "
                                                                                                          "sender "
                                                                                                          "text, "
                                                                                                          "time date)")
                    get_conn.commit()
                    close_connection(Exception)
                    session.pop(request.environ['REMOTE_ADDR'] + 'temp_session_user')
                    session.pop(request.environ['REMOTE_ADDR'] + 'temp_session_email')

                    return "Registration Successfully done  <br/> You can upload your file"
                else:
                    return """
                            <html><body>
                            <h1>Invalid Code</h1><br />
                            <form method='POST'><div>
                            <label id="Code: ">Enter Your Code</label>
                            <input type="text" name="code"/><br />
                            <input type="submit" value="submit" /><br />
                            </div></form></body></html>
                            """
            # elif request.environ['REMOTE_ADDR']+'username' in session:
            #     return render_template("Dashboard.html",name=request.environ['REMOTE_ADDR']+'username')
            else:
                return render_template("Register.html")
        else:
            return """
                                        <html><body>
                                        <h1>Invalid Code</h1><br />
                                        <form method='POST'><div>
                                        <label id="Code: ">Enter Your Code</label>
                                        <input type="text" name="code"/><br />
                                        <input type="submit" value="submit" /><br />
                                        </div></form></body></html>
                                        """
            # else:
            #    return render_template("Dashboard.html",name=session[request.environ['REMOTE_ADDR']+'username'])


@app.route("/<title>", methods=["GET", "POST"])
def find_Friend(title):
    if request.method == "GET":
        if title == 'Add Friends':
            return render_template("AddFriend.html", storage_di=[], val="", title="")
        elif title == 'Req Friends':
            get_req = user_req.get(session[request.environ['REMOTE_ADDR'] + 'username']).strip(",").split(",")
            if "" in get_req:
                get_req.remove("")
            return render_template("ReqFriend.html", storage_di=get_req, title="Req for you: ")
        elif title == "show Friends":
            return render_template("ShowFriends.html", storage_di=user_friends.get(
                session[request.environ['REMOTE_ADDR'] + 'username']).strip(",").split(","))
        else:
            return str(None)
    elif request.method == "POST":
        if title == 'Add Friends':
            search_text = request.form["search_item"]
            add_friend_list = request.form.getlist("ad_fr_list")
            storage_di = dict()
            if len(add_friend_list) > 0:
                for friend_list in add_friend_list:
                    user_req.append(friend_list, session[request.environ['REMOTE_ADDR'] + 'username'] + ",")
            temp_user = session[request.environ['REMOTE_ADDR'] + 'username']
            for friend_u in user_pass.keys(pattern=search_text + "*"):
                if temp_user not in user_req.get(friend_u) \
                        and friend_u not in user_req.get(temp_user) \
                        and friend_u not in user_friends.get(temp_user):
                    storage_di[friend_u] = "Send Request"
            if session[request.environ['REMOTE_ADDR'] + 'username'] in storage_di:
                del storage_di[session[request.environ['REMOTE_ADDR'] + 'username']]
            return render_template("AddFriend.html", storage_di=storage_di, val=search_text, title="Add Friend:- ")
        elif title == 'Req Friends':
            req_list = user_req.get(session[request.environ['REMOTE_ADDR'] + 'username']).strip(",").split(",")
            temp_del_list = []

            for item in req_list:
                li_fri = request.form["rad_li_" + item]
                if li_fri == "Acc":
                    user_friends.append(session[request.environ['REMOTE_ADDR'] + 'username'], item + ",")
                    user_friends.append(item, session[request.environ['REMOTE_ADDR'] + 'username'] + ",")
                    temp_del_list.append(item)
                elif li_fri == "Rej":
                    temp_del_list.append(item)
                else:
                    pass
            for item in temp_del_list:
                req_list.remove(item)
            # map(lambda x:req_list.remove(x),temp_del_list)
            user_req.set(session[request.environ['REMOTE_ADDR'] + 'username'], ",".join(req_list) + ",")
            # return str(True)
            if "" in req_list:
                req_list.remove("")
            return render_template("ReqFriend.html", storage_di=req_list, title="Req for you: ")
    else:
        return render_template("ImageDisplay.html")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    if request.environ['REMOTE_ADDR'] + 'username' in session:
        if request.method == "POST":
            session.pop(request.environ['REMOTE_ADDR'] + 'username', None)
            return """
            <html><body>
            <h1>Logout Successfully</h1>
            <h2><a href='""" + url_for('login') + """'>Login</a>
            </body></html>
            """
        else:
            return render_template("Dashboard.html", name=session[request.environ['REMOTE_ADDR'] + 'username'])
    else:
        return render_template("Login.html")


def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def cal_size(file_name):
    if os.path.isfile(file_name):
        file_info = os.stat(file_name)
        return convert_bytes(file_info.st_size)


@app.route("/ChatFriend", methods=["GET"])
def ChatFriend():
    if request.method == "GET":
        db_c = get_db()
        db_cu = db_c.cursor()

        user_name = (request.args['button'])[10:]
        data1 = db_cu.execute("SELECT * FROM " + session[
            request.environ[
                'REMOTE_ADDR'] + 'username'] + " WHERE sender = '" + user_name + "' UNION ALL " + "SELECT * FROM " + user_name + "  WHERE sender = '" +
                              session[
                                  request.environ['REMOTE_ADDR'] + 'username'] + "' ORDER BY time ASC")
        #data1 = db_cu.execute("SELECT * FROM " + session[
        #    request.environ['REMOTE_ADDR'] + 'username'] + " WHERE sender = '" + user_name + "'")
        #
        data1 = data1.fetchall()
        #data2 = db_cu.execute("SELECT * FROM "+user_name+"  WHERE sender = '" +session[request.environ['REMOTE_ADDR'] + 'username'] +"'")
        #data2 = data2.fetchall()
        #data1.extend(data2)
        close_connection(Exception)
        assert isinstance(user_name, str)
        return render_template("Messages.html",
                               msg=data1,
                               title=user_name
                               )


@app.route("/messages<title>", methods=["GET", "POST"])
def messages(title):
    date = datetime.now()
    db_c = get_db()
    db_cu = db_c.cursor()

    data1 = db_cu.execute("SELECT * FROM " + session[
        request.environ['REMOTE_ADDR'] + 'username'] + " WHERE sender = '" + title + "' UNION ALL "+"SELECT * FROM " + title + "  WHERE sender = '" + session[
        request.environ['REMOTE_ADDR'] + 'username'] + "' ORDER BY time ASC")
    data1 = data1.fetchall()
    #data2 = db_cu.execute("SELECT * FROM " + title + "  WHERE sender = '" + session[
    #    request.environ['REMOTE_ADDR'] + 'username'] + "'")
    #data2 = data2.fetchall()
    #data1.extend(data2)
    if request.method == "GET":

        close_connection(Exception)
    elif request.method == "POST":

        text_area_resp = request.form["text_area"]
        db_cu.execute("INSERT INTO " + title + " VALUES('" + text_area_resp + "','" + session[
            request.environ['REMOTE_ADDR'] + 'username'] + "','" + str(date) + "')")
        db_c.commit()
        close_connection(Exception)
        data1.append((text_area_resp,session[request.environ['REMOTE_ADDR'] + 'username'],str(date)))
    return render_template("Messages.html",
                           msg=data1,
                           title=title
                           )


@app.errorhandler(404)
def page_not_found():
    return render_template("ImageDisplay.html", name="404-snake.png"), 404


@app.route("/test", methods=["GET", "POST"])
def test_admin():
    if request.method == "GET":
        return ("<html> \n"
                "            <body>\n"
                "            <form method='post'>\n"
                "            <input type=\"password\" name=\"password\"/>\n"
                "            <input type=\"submit\" value=\"back to dashboard\" />\n"
                "            </form>\n"
                "            </body>\n"
                "            </html>")
    elif request.method == "POST":
        if request.form["password"] == "admin's password" and "Mozilla" in request.headers['User-Agent']:
            return str(request.headers['User-Agent'])
        else:
            return render_template("Login.html")
