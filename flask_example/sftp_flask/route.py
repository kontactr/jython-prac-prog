import os
import urllib.request
from glob import glob
import requests
import redis
from flask import current_app, send_from_directory
from flask import render_template
from werkzeug.utils import secure_filename
import json
from __init__ import app
from datetime import datetime
from decimal import *


"""import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText"""
from SendMail import send_mail_multiple
from GoogLog import *
from GoogDrive import *
from FileType import *
from urllib3.request import RequestMethods
import urllib3

# username_session = None
# code = None
r_conn = redis.StrictRedis(db=1, charset="utf-8", decode_responses=True)
file_conn = redis.StrictRedis(db=2, charset="utf-8", decode_responses=True)
e_conn = redis.StrictRedis(db=3, charset="utf-8", decode_responses=True)
folder_conn = redis.StrictRedis(db=11, charset="utf-8", decode_responses=True)
session_conn = redis.StrictRedis(db=12,charset="utf-8", decode_responses=True)

#print ("hello "+session)

@app.route("/", methods=["GET"])
def home():
    if request.environ['REMOTE_ADDR'] + 'username' not in session:
        return """<html>
        <body>
            <a href='""" + url_for("login") + """'>Login Page</a>
        </body>
        </html>"""+str(request.user_agent)
    else:

        return render_template("Dashboard.html", name=session[request.environ['REMOTE_ADDR'] + 'username'])


@app.route("/login", methods=["GET", "POST"])
def login():
    # global username_session
    if request.environ['REMOTE_ADDR'] + 'username' not in session:
        if (request.method == "GET"):
            return render_template("Login.html")

        elif (request.method == "POST"):
            username = request.form["username"]
            #username = request.Username;

            password = request.form["password"]
            #password = request.Password;
            if (password == r_conn.get(username)):

                session[request.environ['REMOTE_ADDR'] + 'username'] = username
                # username_session = username

                return  render_template("Dashboard.html", name=session[request.environ['REMOTE_ADDR'] + 'username'])
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
    s.login("ch.email.456@gmail.com", "ch.email.456")
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
                    if (r_conn.exists(username)):
                        return "<h1>Username is already taken.</h1><br/>" + render_template("Register.html")
                    else:
                        send_mail(email)
                        session[request.environ['REMOTE_ADDR'] + 'temp_session_user'] = username
                        session[request.environ['REMOTE_ADDR'] + 'temp_session_password'] = password
                        session[request.environ['REMOTE_ADDR'] + 'temp_session_email'] = email
                except Exception as e:
                    if (request.environ['REMOTE_ADDR'] + 'temp_session_user' in session):
                        session.pop(request.environ['REMOTE_ADDR'] + 'temp_session_user')
                    if (request.environ['REMOTE_ADDR'] + 'temp_session_password' in session):
                        session.pop(request.environ['REMOTE_ADDR'] + 'temp_session_password')
                    if (request.environ['REMOTE_ADDR'] + 'temp_session_email' in session):
                        session.pop(request.environ['REMOTE_ADDR'] + 'temp_session_email')
                    return str(e) + render_template("Register.html")

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
                    r_conn.set(session[request.environ['REMOTE_ADDR'] + 'temp_session_user'],
                               session[request.environ['REMOTE_ADDR'] + 'temp_session_password'])
                    e_conn.set(session[request.environ['REMOTE_ADDR'] + 'temp_session_user'],
                               session[request.environ['REMOTE_ADDR'] + 'temp_session_email'],
                               )
                    session.pop(request.environ['REMOTE_ADDR'] + 'temp_session_password')
                    os.mkdir("Data\\" + session[request.environ['REMOTE_ADDR'] + 'temp_session_user'])
                    file_conn.set(session[request.environ['REMOTE_ADDR'] + 'temp_session_user'], "")
                    session_conn.set(session[request.environ['REMOTE_ADDR'] + 'temp_session_user'],"")
                    session.pop(request.environ['REMOTE_ADDR'] + 'temp_session_user')
                    session.pop(request.environ['REMOTE_ADDR'] + 'temp_session_email')

                    return "Registration Successfully done  <br/> You can upload your file" + """
                <html><body>
                <form method='get' action='""" + url_for('login') + """'>
                <input type='submit' value='Goto Login' /></form>
                </body></html>
            """
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


@app.route("/logout", methods=["GET", "POST"])
def logout():
    if request.environ['REMOTE_ADDR'] + 'username' in session:
        if request.method == "POST":
            session.pop(request.environ['REMOTE_ADDR'] + 'username', None)
            if request.environ['REMOTE_ADDR'] + 'goog_session' in session:
                session.pop(request.environ['REMOTE_ADDR'] + 'goog_session')
                return redirect(url_for('logout_google'))
            return """
            <html><body>
            <h1>Logout Successfully</h1>
            <h2><a href='""" + url_for('login') + """'>Login</a>
            </body></html>
            """
        else:
            return render_template("Dashboard.html", name=session[request.environ['REMOTE_ADDR'] + 'username'])
    else:
        return redirect(url_for('login'))


@app.route("/upload/<path_dir>", methods=[ "POST"])
def upload(path_dir):
    if request.environ['REMOTE_ADDR'] + 'username' in session:
        #if request.method == "GET":
        #    size = 0
        #    storage_di = dict()
        #    for item in glob("Data\\" + session[request.environ['REMOTE_ADDR'] + 'username'] + "/*"):
        #        storage_di[item.split("\\")[-1]] = cal_size(item)
        #        size += os.stat(item).st_size
        #   return render_template("Upload.html", size=1024 * 1024 * 1024 - size)
        if request.method == "POST":
            file1 = request.files.getlist("file")

            for file in file1:
                if (len("" + str(file.filename) + "a") <= 1):
                    return redirect(url_for('show_files',user_pa=path_dir))
                else:
                    filename = secure_filename(file.filename)
                    if(path_dir[-1] != '\\'):
                        path_dir += "\\"
                    file.save(os.path.join(path_dir, filename))
                    if path_dir == "Data\\"+session[request.environ['REMOTE_ADDR'] + 'username']+"\\":
                        file_conn.append(session[request.environ['REMOTE_ADDR'] + 'username'],
                                         filename+","
                                         )
                    else:
                        folder_conn.append(
                            path_dir[:-1:]+"$"+session[request.environ['REMOTE_ADDR'] + 'username'],
                            filename+","
                        )
            else:
                return render_template("Confirmation.html", type_of_con="File Successfully Uploaded",
                                       return_url="Login", msg="Go to Dashboard")

    else:
        return render_template("Login.html")




@app.route("/data/<user_pa>")
def show_files(user_pa):
    if request.environ['REMOTE_ADDR'] + 'username' in session:
        user_path = ""

        folder_list_p = []
        file_list = []
        if user_pa == '\\' or user_pa == "Data\\"+session[request.environ['REMOTE_ADDR'] + 'username']+ '\\' :

                user_path = "Data\\"+session[request.environ['REMOTE_ADDR'] + 'username']+ '\\'
                file_list = file_conn.get(
                    session[request.environ['REMOTE_ADDR'] + 'username']).strip(",").split(",")

                for j in file_list:
                    if "." not in j:
                        folder_list_p.append(j)
                file_list = set(file_list).difference(set(folder_list_p))
        else:

            user_path =  user_pa
            file_list = folder_conn.get(
                user_pa+"$"+session[request.environ['REMOTE_ADDR'] + 'username']
            )
            if file_list == None:
                file_list = []
            else:
                file_list = file_list.strip(",").split(",")
            for j in file_list:
                if "." not in j:
                    folder_list_p.append(j)
            file_list = set(file_list).difference(set(folder_list_p))

        return render_template("FilesDisplay.html",
                               name=session[request.environ['REMOTE_ADDR'] + 'username'],
                               name1=session[request.environ['REMOTE_ADDR'] + 'username'],
                               file_list=list(file_list),
                               folder_list = folder_list_p,
                               msg="Go to Dashboard",
                               dir_path=user_path
                               ) + str(user_path)
    else:
        return render_template("Login.html")

@app.route("/data/temp_route/<val1>/<val2>")
def temp_route(val1,val2):
    if (val1[-1] == '\\'):
        return redirect(url_for('show_files',user_pa=str(val1+val2)))
    else:
        return redirect(url_for('show_files', user_pa=str(val1 + "\\"+ val2)))

def def_file(di , storage_di):
    if (os.path.isfile(di)):
        storage_di[di.split("\\")[-1]] = cal_size(di)
        return storage_di
    else:
        for k in glob(di+"/*"):

            def_file(k , storage_di)


def controller_def_file(path):
    storage_di = dict()
    size = 0
    di_obj = def_file(path , storage_di)
    return (storage_di)
    #size += os.stat(item).st_size


def single_dir(path):
    storage_di = {}
    for item in glob(path+"/*"):
        storage_di[item.split("\\")[-1]] = cal_size(item)
    return storage_di


def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def cal_size(file_name):
    if os.path.isfile(file_name):
        file_info = os.stat(file_name)
        return convert_bytes(file_info.st_size)


@app.route("/storage/<path>", methods=["GET", "POST"])
def show_storage(path):
    if request.environ['REMOTE_ADDR'] + 'username' in session:
        if request.method == "GET":


            return render_template("ShowStorage.html", storage_di=single_dir(
                path), total_size=0, dir_path = path.strip("\\"))

        elif request.method == "POST":
            path += "\\"
            delete_list = request.form.getlist('sh_fi')
            storage_list = []
            flag = True
            if path == "Data\\"+session[request.environ['REMOTE_ADDR'] + 'username']+"\\":
                storage_list = file_conn.get(session[request.environ['REMOTE_ADDR'] + 'username']).strip(",").split(",")

            else:

                storage_list = folder_conn.get(path[:-1:]+"$"+session[request.environ['REMOTE_ADDR'] + 'username']).strip(",").split(",")
                flag = False
            if (len(delete_list) > 0):
                for file in delete_list:
                    if file in storage_list:
                        storage_list.remove(file)
                        os.remove(path + file)
                if(flag):
                    file_conn.set(session[request.environ['REMOTE_ADDR'] + 'username'],
                              ",".join(storage_list) + ",")
                else:
                    folder_conn.set(path[:-1:]+"$"+session[request.environ['REMOTE_ADDR'] + 'username'],
                                    ",".join(storage_list) + ",")
                return render_template("Confirmation.html", type_of_con="Operation Successfully Done.",
                                       msg="Go to Dashboard")
            else:
                #return (path)
                return render_template("ShowStorage.html", storage_di=single_dir(
                    path), total_size=0, dir_path=path.strip("\\"))
                #return render_template("ShowStorage.html", storage_di=storage_di, total_size=0)
    else:
        return render_template("Login.html")


@app.route("/email/<path>", methods=["GET", "POST"])
def send_email_data(path):
    if request.environ['REMOTE_ADDR'] + 'username' in session:
        if request.method == "POST":
            mail_files = request.form.getlist('sh_fi')
            if (mail_files != None and len(mail_files) > 0):
                for index in range(0, len(mail_files)):
                    mail_files[index] = path + \
                                        mail_files[index]
                send_mail_multiple(mail_files,
                                   e_conn.get(session[request.environ['REMOTE_ADDR'] + 'username']),
                                   session[request.environ['REMOTE_ADDR'] + 'username'])
                return render_template("Confirmation.html", type_of_con="File Successfully Uploaded",
                                       return_url="Login", msg="Successfully Sended to your MailBox")
            else:
                storage_di = dict()
                size = 0
                return render_template("ShowStorage.html", storage_di=single_dir(
                    path), total_size=0, dir_path=path.strip("\\"))
                #return render_template("ShowStorage.html", storage_di=storage_di, total_size=size,
                #                       dir_path = path)
    else:
        return render_template("Login.html")


@app.route('/download/<dirc>/<filename>', methods=['GET'])
def download(dirc, filename):
    uploads = os.path.join(current_app.root_path,  dirc)
    return send_from_directory(directory=uploads, filename=filename)


@app.route('/gen_pub_url', methods=["post"])
def get_pub_url():
    if request.environ['REMOTE_ADDR'] + 'username' in session:
        if request.method == "POST":
            mail_files = request.form.getlist('sh_fi')
            if (mail_files != None and len(mail_files) > 0):
                url = session[request.environ['REMOTE_ADDR'] + 'username'] + "/" + "files="
                url += ";".join(mail_files)
                return """
                    <html>
                    <body><h1>Your Public URL: </h1></body>
                    <h3>/public/
                """ + url + """</h3></body></html>"""
            else:
                storage_di = dict()
                for item in glob("Data\\" + session[request.environ['REMOTE_ADDR'] + 'username'] + "/*"):
                    storage_di[item.split("\\")[-1]] = cal_size(item)
                return render_template("ShowStorage.html", storage_di=storage_di)

    else:
        return render_template("Login.html")


@app.route('/public/<url>/<data>', methods=['GET'])
def public(url, data):
    # return str(len(url))
    if request.environ['REMOTE_ADDR'] + 'username' in session:
        return render_template("FilesDisplay.html",
                               name="Public Data",
                               file_list=data.strip(" ")[6:].split(";"),
                               msg="Go to Dashboard",
                               name1=url.strip(" "),
                               dir_path = ""
                               )
    else:
        return render_template("Login.html")


@app.route('/goog_settings/<data_obj>',methods=["GET"])
def goog_settings(data_obj):
    # 0 - name , 1 - email
    if request.method == "GET":
        try:
            temp = data_obj.split("[]")
            if temp[0] == '':
                temp[0] = (temp[1].split("@"))[0]
            if (temp[2] == r_conn.get(temp[0])):
                session[request.environ['REMOTE_ADDR'] + 'username'] = temp[0]
                # username_session  = username

                return render_template("Dashboard.html", name=session[request.environ['REMOTE_ADDR'] + 'username'])
            else:
                r_conn.set(temp[0], temp[2])
                e_conn.set(temp[0], temp[1])
                os.mkdir("Data\\" + temp[0])
                file_conn.set(temp[0], "")
                session[request.environ['REMOTE_ADDR'] + 'username'] = temp[0]
                return redirect(url_for('login'))
        except Exception as e:
            return str(e)
    else:
        return redirect(url_for('login'))


def file_format(file_name,user_name):
    return "Data\\"+user_name+"\\"+file_name

@app.route("/<name>/upload_request/<path>",methods=["GET","POST"])
def upload_drive_files(name,path):
    if request.method == "GET":

        return render_template("DriveUploadFiles.html", list_item=single_dir(
            path), total_size=0, path=path.strip("\\"), name=name)

        #storage_di = dict()
        #for item in glob("Data\\" + session[request.environ['REMOTE_ADDR'] + 'username'] + "/*"):
        #    storage_di[item.split("\\")[-1]] = cal_size(item)
        #return render_template("DriveUploadFiles.html" , name=name , storage_di=storage_di)
    if request.method == "POST":

        if name == "Google":
            upload_files = request.form.getlist('sh_fi')
            if (upload_files != None and len(upload_files) > 0):
                with open('Credentials\\'+session[request.environ['REMOTE_ADDR'] + 'username']+"credentials.json") as data_file:
                    data = json.load(data_file)
                for file in upload_files:

                    attachment ,maintype = file_type(file_format(file,path[5::]))
                    http = httplib2.Http()
                    http = get_credentials().authorize(http)

                    drive_service = build('drive', 'v3', http=http)
                    #return (path)
                    media_body = MediaFileUpload(path+"//"+file, mimetype='text/plain', resumable=True)
                    body = {
                        'name' : file,
                        'title': file,
                        'description': 'A test document',
                        'mimeType': maintype
                    }

                    file1 = drive_service.files().create(body=body, media_body=media_body).execute()
                    #drive_service.files().create(media_body='pig.png', body={'name': 'pig'}).execute()
                return render_template("Confirmation.html",msg="Goto Your Dashboard", type_of_con = "Successfully Uploaded Files"+
                                                                                                " In Your Another "+
                                                                                                "Storage")

                """
                    r = requests.post(url="https://www.googleapis.com/upload/drive/v3?uploadType=media",
                                        data=attachment.__bytes__(),
                                      headers={"User-Agent": "", "Content-Type": str(maintype), "Content-Length": str(os.stat(
                                          file_format(file, session[
                                              request.environ['REMOTE_ADDR'] + 'username'])).st_size),
                                               "Authorization": data["access_token"]}
                                      )
                    return (str(r.request))"""
                """ req = urllib.request.Request(method="POST",
                                                 headers={"User-Agent":"","Content-Type": maintype, "Content-Length": os.stat(
                                                     file_format(file, session[
                                                         request.environ['REMOTE_ADDR'] + 'username'])).st_size,
                                                          "Authorization": data["access_token"]} ,
                                                 url="https://www.googleapis.com/upload/drive/v3?uploadType=media HTTP/1.1",
                                                 data=attachment.__bytes__()
                                                 )"""
                """   #resp = urllib.request.urlopen(req)
                    #https = RequestMethods(headers={"Content-Type":maintype,"Content-Length":os.stat(file_format(file,session[request.environ['REMOTE_ADDR'] + 'username'])).st_size,
                     #                                      "Authorization":data["access_token"]})
                    #Resp = https.urlopen(method="POST",
                     #                             url="https://www.googleapis.com/upload/drive/v3?uploadType=media",
                     #                             body=attachment
                     #                             )
                     #return "0B3Qd1rlyIyR5bHo0dENpM1lSclk"""





@app.route("/<name>/download_request/<path>",methods=["GET","POST"])
def download_drive_files(name,path):
    if request.method == "GET":
         path = "'"+path+"'"
         all_files = fetch(path+" in parents and (mimeType = 'application/vnd.google-apps.folder' or mimeType != 'application/vnd.google-apps.folder')",
                              sort='modifiedTime desc')
         list_item = {}
         for file in all_files:
             #s += "%s, %s<br>" % (file['name'], file['id'])
             list_item[file['id']] = file['name']
         #return s
         #download_drive_file("0B5DUSJ7ypnG8V19sb180T18zNms","Data\\"+session[request.environ['REMOTE_ADDR'] + 'username']
         #                    +"\\"+"Temp.pdf")
         #return str(list_item)
         return render_template("DriveShowStorage.html",list_item=list_item,path=path)

    elif request.method == "POST":
        file_download_list = request.form.getlist('sh_fi')
        st_file = ""
        for file_do in file_download_list:
            temp_po = file_do.split(" ")
            download_drive_file(temp_po[0],
                            "Data\\"+session[request.environ['REMOTE_ADDR'] + 'username']+"\\"+
                                " ".join(temp_po[1::]))
            st_file += " ".join(temp_po[1::])+","
        file_conn.set(
            session[request.environ['REMOTE_ADDR'] + 'username'],
            file_conn.get(session[request.environ['REMOTE_ADDR'] + 'username'])+st_file
        )
        return render_template("Confirmation.html",type_of_con = "Successfully Downloaded In Your Home Directory",
                               msg="GoTo Your Dashboard")


    else:
        redirect(url_for("login"))




@app.route("/temp/redirect")
def temp_redirect():
    return redirect('goog_drive_auth', session[request.environ['REMOTE_ADDR'] + 'username'])


@app.errorhandler(404)
def page_not_found(e):
    return render_template("ImageDisplay.html", name="404-snake.png"), 404


@app.route("/data/<flag>/<dir_path>",methods=["POST"])
def create_dir(flag,dir_path):
    if flag == "True":
        if dir_path == "Data\\"+session[request.environ['REMOTE_ADDR'] + 'username']+"\\":
            if not os.path.exists(dir_path + request.form["name_dir"]):
                file_conn.append(session[request.environ['REMOTE_ADDR'] + 'username'], str(
                request.form["name_dir"]
                ) + ",")

                os.makedirs(dir_path+request.form["name_dir"])
                folder_conn.set(dir_path + request.form["name_dir"] + "$" + session[request.environ['REMOTE_ADDR'] + 'username'], "")

                return redirect(url_for('show_files', user_pa=dir_path))

        else:
            temp = dir_path

            if folder_conn.exists(dir_path+"$"+session[request.environ['REMOTE_ADDR'] + 'username']):
                os.makedirs(temp + "\\" + request.form["name_dir"])
                var_temp = folder_conn.get(dir_path+"$"+session[request.environ['REMOTE_ADDR'] + 'username'])
                var_temp += request.form["name_dir"] +","
                folder_conn.set(dir_path+"$"+session[request.environ['REMOTE_ADDR'] + 'username'],var_temp)
                folder_conn.set(temp + "\\" + request.form["name_dir"]+"$"+session[request.environ['REMOTE_ADDR'] + 'username'],"")

                return redirect(url_for('show_files',user_pa=temp))
            else:

                os.makedirs(temp +"\\" +request.form["name_dir"])
                folder_conn.set(dir_path+"\\" +request.form["name_dir"]+"$"+session[request.environ['REMOTE_ADDR'] + 'username'], "")

            return redirect(url_for('show_files'  ,user_pa=temp))



@app.route("/profile",methods=["GET","POST"])
def profile():
    if request.environ['REMOTE_ADDR'] + 'username' in session:
        if request.method == "GET":
            return render_template("Profile.html",
                                   name = session[request.environ['REMOTE_ADDR'] + 'username'],
                                   email = e_conn.get(session[request.environ['REMOTE_ADDR'] + 'username']))

        elif request.method == "POST":
            name = request.form["name"]
            email = request.form["email"]
            if len(str(email)) != 0 and email != e_conn.get([session[request.environ['REMOTE_ADDR'] + 'username']]):
                import smtplib as se
                from email.mime.multipart import MIMEMultipart
                from email.mime.text import MIMEText
                s = se.SMTP_SSL('smtp.gmail.com')
                msg = MIMEMultipart('alternative')
                msg['Form'] = "ch.email.456@gmail.com"
                msg['To'] = email
                msg_part = MIMEText("Mail Successfully Changed")
                msg.attach(msg_part)
                s.login("ch.email.456@gmail.com", "ch.email.456")
                s.sendmail("ch.email.456@gmail.com", email, msg.as_string())
                s.quit()
                e_conn.set(session[request.environ['REMOTE_ADDR'] + 'username'],email)



            if (request.form["password"] == request.form["cpassword"]):
                if len("" + request.form["password"]) != 0:
                    r_conn.set(session[request.environ['REMOTE_ADDR'] + 'username'],request.form["password"])


            if len(str(name)) != 0 and r_conn.get(name) == None:
                var_temp_profile = session[request.environ['REMOTE_ADDR'] + 'username']
                r_pass = r_conn.get(var_temp_profile)
                r_conn.delete(var_temp_profile)
                r_conn.set(name,r_pass)
                r_pass = e_conn.get(var_temp_profile)
                e_conn.delete(var_temp_profile)
                e_conn.set(name,r_pass)
                r_pass = file_conn.get(var_temp_profile)
                file_conn.delete(var_temp_profile)
                file_conn.set(name,r_pass)
                r_pass = session_conn.get(var_temp_profile)
                session_conn.delete(var_temp_profile)
                session_conn.set(name,r_pass)
                session[request.environ['REMOTE_ADDR'] + 'username'] = name

                r_pass = folder_conn.keys("Data?"+var_temp_profile+"*"+"$"+var_temp_profile)
                for j in r_pass:
                    folder_data = folder_conn.get(j)
                    temp = j.split("\\")
                    temp[1] = name
                    temp = "\\".join(temp)
                    temp = temp.split("$")
                    temp[-1] = name
                    temp = "$".join(temp)
                    folder_conn.delete(j)
                    folder_conn.set(temp,folder_data)

                os.rename("Data\\"+var_temp_profile,"Data\\"+name)

            return redirect(url_for("login"))




        else:
            return redirect(url_for('profile'))
    else:
        return redirect(url_for('login'))


@app.route("/location_store",methods=["POST"])
def location_store():
     if request.environ['REMOTE_ADDR'] + 'username' in session:
         if request.method == "POST":
             loca = list(map(lambda x:x.strip(" "),request.form["location"].strip(" ").split("-")))
             if session_conn.exists(session[request.environ['REMOTE_ADDR'] + 'username']):
                 val = str(loca[1])+" "+str(loca[2])+" "+str(datetime.now())+","
                 session_conn.set(session[request.environ['REMOTE_ADDR'] + 'username'],
                                  session_conn.get(session[request.environ['REMOTE_ADDR'] + 'username'])+val
                                  )
             else:
                 session_conn.set(session[request.environ['REMOTE_ADDR'] + 'username'],str(loca[1])+" "+str(loca[2])+" "+str(datetime.now())+",")

             return redirect("login")
         else:
             return redirect("profile")
     else:
        return redirect("login")

@app.route("/get_google_map",methods=["POST"])
def get_google_map():
    google_location = []
    for x,y in enumerate(session_conn.get(session[request.environ['REMOTE_ADDR'] + 'username']).split(",")[:-1:]):
        temp = [""]

        temp.extend ( y.split(" ")[:-2:])
        temp.append(x)
        google_location.append(temp)

    return render_template("GoogleMaps.html",data = json.dumps(google_location))




@app.route("/test", methods=["GET", "POST"])
def test_admin():
    if request.method == "GET":
        return """<html> 
            <body>
            <form method='post'>
            <input type="password" name="password"/>
            <input type="submit" value="back to dashboard" />
            </form>
            </body>
            </html>"""
    elif request.method == "POST":
        #if request.form["password"] == "password" and "Mozilla" in request.headers['User-Agent']:
            #return str(session[request.environ['REMOTE_ADDR'] + 'goog_session'])
            #return str(request.headers['User-Agent'])
        #else:
         #   return render_template("Login.html")
        #file_list = file_conn.append("ch1",",")
        #file_list = file_conn.get("ch1")
        #file_list = file_list[:-1:]
        #file_conn.set("ch1",file_list)
        return str(folder_conn.keys("*$"+"ch9"))

        return "True"

