import os
import urllib.request
from glob import glob
import requests
import redis
from flask import current_app, send_from_directory, request, session, url_for, send_file
from flask import render_template
from werkzeug.utils import secure_filename, redirect
import json
from __init__ import app
from ExternalFunction import *
from datetime import datetime
from decimal import *
from GoogDrive import *
from FileType import *
from urllib3.request import RequestMethods
import urllib3
from SendMail import send_mail_multiple


r_conn = redis.StrictRedis(db=5, charset="utf-8", decode_responses=True)

user_conn = redis.StrictRedis(db=14, charset="utf-8", decode_responses=True)

session_conn = redis.StrictRedis(db=15, charset="utf-8", decode_responses=True)

user_directory = redis.StrictRedis(db=13, charset="utf-8", decode_responses=True)

location_conn = redis.StrictRedis(db=6, charset="utf-8", decode_responses=True)

rsa_conn = redis.StrictRedis(db=8, charset="utf-8", decode_responses=True)


@app.route("/")
def home():
    return redirect("login",code=302)


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        if request.headers['User-Agent'] == 'Mobile':
            return "Done"
        else:
            if request.environ['REMOTE_ADDR'] + 'session_user' not in session:
                return render_template("Login.html")
            else:
                return redirect("dashboard")

    elif request.method == "POST":
        if user_conn.get(request.form["username"]) == request.form["password"]:
            session[request.environ['REMOTE_ADDR'] + 'session_user'] = request.form["username"]
            session[request.environ['REMOTE_ADDR'] + 'user_dir'] = user_directory.get(session[request.environ['REMOTE_ADDR'] + 'session_user'])
            session_conn.set(session[request.environ['REMOTE_ADDR'] + 'session_user'],
                             session_conn.get(session[request.environ['REMOTE_ADDR'] + 'session_user']) +
                             request.environ['REMOTE_ADDR'] + ",")

            
            return redirect("dashboard")

        else:
            return redirect("login")

    else:
        return redirect("login")


@app.route("/dashboard", methods=["GET"])
def dashBoard():
    if request.environ['REMOTE_ADDR'] + 'session_user' not in session:
        return redirect("login")
    else:
        if request.method == "GET":
            return render_template("DashBoard.html",path=session[request.environ['REMOTE_ADDR'] + 'user_dir']
                                   )


@app.route("/viewdata/<path>", methods=["GET"])
def view_data(path):
    if request.environ['REMOTE_ADDR'] + 'session_user' not in session:

        return redirect("login")
    else:
        if request.method == "GET":
            folder_dir , file_dir = single_dir(path.strip(" "))
            return render_template("ShowStorage.html",
                                   dir_path = path.strip(" "),
                                   file_dir = file_dir,
                                   folder_dir = folder_dir
                                )
        else:
            return redirect("login")

@app.route("/uploaddata/<path>", methods=["GET","POST"])
def upload_data(path):
    if request.method == "POST":
        
        file1 = request.files.getlist("file")
        
        for file in file1:
            if (len("" + str(file.filename) + "a") <= 1):
                return redirect(url_for('view_data', path=path))
            else:
                filename = secure_filename(file.filename)
                
                file.save(os.path.join(path, filename))

        return redirect(url_for('view_data', path=path))
    else:
        return redirect("login")

@app.route("/create_dir/<path>",methods=["POST"])
def create_dir(path):
    if len (request.form["name_dir"]) > 0:
        try:
            os.makedirs(path+"\\"+request.form["name_dir"])

            return redirect(url_for("view_data",path=path))
        except Exception as e:
            return str(e)

@app.route("/delete_file/<path>",methods=["POST"])
def delete_file(path):
    if request.method == "POST":
        delete_files =  request.form.getlist('sh_fi')
        except_items = []
        if (delete_files != None and len(delete_files) > 0):
            for item in delete_files:
                try:
                    if os.path.isfile(path+"\\"+item):
                        os.remove(path+"\\"+item)
                    elif os.path.isdir(path+"\\"+item):
                        os.removedirs(path+"\\"+item)
                    else:
                        os.remove(path + "\\" + item)
                except:
                    except_items.append(item)
            if (len(except_items) == 0):
                return redirect(url_for("view_data", path=path))
            else:
                return render_template("ExceptionList.html",file_list=except_items)
        else:
            return redirect(url_for("view_data",path=path))
    else:
        return redirect("login")


@app.route("/download/<path>",methods=["POST"])
def download_file(path):

    if request.method == "POST":
        compress_type = request.form["radio"]
        select_list = request.form.getlist("sh_fi")

        if ( len(select_list) == 1  and os.path.isfile(path+"\\"+select_list[0]) ):
            return send_file(os.path.join(path+"\\",select_list[0]),as_attachment=True)

        
        if (compress_type.strip(" ") == "Deep Compress"):

            if select_list != None and len(select_list) > 0 :
                folder_list = []
                main_dict = {path:[]}
                for item in select_list:
                    if  check_folder(path+"\\"+item):
                        main_dict.update(round_fun(path+"\\"+item,{path+"\\"+item:[]}))
                    main_dict[path].append(path+"\\"+item)

                zip_file = "-".join(str( datetime.now().time() ).split(":")[:3])+".zip"
                remove_dir = [os.path.join(path, zip_file)]

                myZipFile = zipfile.ZipFile(zip_file,"w",zipfile.ZIP_DEFLATED)
                make_zip(path,myZipFile,main_dict,remove_dir)
                myZipFile.close()
                myThread(remove_dir).start()
                return send_file(os.path.join(os.getcwd(), zip_file),as_attachment=True)
                #return redirect(url_for("view_data",path=path))

            else:
                    return redirect(url_for("view_data",path=path))

        else:
            if select_list != None and len(select_list) > 0 :
                got_tar_file = str(build_tar_file(path,select_list))
                myThread([got_tar_file]).start()
                return send_file(os.path.join(os.getcwd(), got_tar_file),as_attachment=True)
            else:
                return redirect(url_for("view_data",path=path))
    else:
        return redirect("login")




@app.route("/Config",methods=["GET","POST"])
def config_data():
    if request.method == "GET":
        return render_template("Settings.html")

    elif request.method == "POST":
        user_directory.set(session[request.environ['REMOTE_ADDR'] + 'session_user' ] ,
            request.form["Directory"])
        session[request.environ['REMOTE_ADDR'] + 'user_dir'] = user_directory.get(session[request.environ['REMOTE_ADDR'] + 'session_user'])
        return redirect(url_for("home"))

@app.route("/logout",methods=["POST"])
def logout():
        session.pop(request.environ['REMOTE_ADDR'] + 'session_user')
        return  redirect("/")


@app.route("/uploadfolder/<path>",methods=["POST"])
def upload_folder(path):
    if request.method == "POST":
        folder_list = request.files.getlist("folder")
        for item in folder_list:
            if ".zip" in item.filename.lower():
                filename = secure_filename(item.filename)
                item.save(os.path.join(path, filename))
                #os.makedirs(os.path.join(path, filename[:-4]))
                extract_folder(path+"\\",filename)
                os.remove(os.path.join(path, filename))

    return redirect(url_for("view_data",path=path))


#---------- New Update ---------------#

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
    if request.environ['REMOTE_ADDR'] + 'session_user' not in session:
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

                return redirect(url_for("next_step"))

            else:
                return render_template("Register.html")
        else:
            return render_template("Register.html")
    else:
        return render_template("Dashboard.html", name=session[request.environ['REMOTE_ADDR'] + 'username'])


@app.route("/register/validate", methods=["GET", "POST"])
def next_step():
    if request.environ['REMOTE_ADDR'] + 'session_user' in session:
        return render_template("Dashboard.html", name=session[request.environ['REMOTE_ADDR'] + 'username'])
    else:
        if request.method == "GET":



            if request.environ['REMOTE_ADDR'] + '_' + 'code' in session:



                if request.args.get("send") == "Resend Code":

                    send_mail(session[request.environ['REMOTE_ADDR'] + 'temp_session_email'])


                return """
                <html><body>
                <form method='POST'><div>
                <label id="Code: ">Enter Your Code</label>
                <input type="text" name="code"/><br />
                <input type="submit" value="submit" /><br />
                <input type="submit" name="send" value="Resend Code" formaction='""" + url_for('next_step') + """'
                formmethod="get">
                </div></form></body></html>
                """
            else:
                return render_template("Register.html")
        elif "POST" == request.method:
            if request.environ['REMOTE_ADDR'] + '_' + 'code' in session:
                if session[request.environ['REMOTE_ADDR'] + '_' + 'code'] == request.form["code"]:
                    session.pop(request.environ['REMOTE_ADDR'] + '_' + 'code')
                    user_conn.set(session[request.environ['REMOTE_ADDR'] + 'temp_session_user'],
                               session[request.environ['REMOTE_ADDR'] + 'temp_session_password'])
                    r_conn.set(session[request.environ['REMOTE_ADDR'] + 'temp_session_user'],
                               session[request.environ['REMOTE_ADDR'] + 'temp_session_email'],
                               )
                    session.pop(request.environ['REMOTE_ADDR'] + 'temp_session_password')

                    user_directory.set(session[request.environ['REMOTE_ADDR'] + 'temp_session_user'], "C:\\")
                    session_conn.set(session[request.environ['REMOTE_ADDR'] + 'temp_session_user'],"")
                    location_conn.set(session[request.environ['REMOTE_ADDR'] + 'temp_session_user'], "")
                    rsa_conn.set(session[request.environ['REMOTE_ADDR'] + 'temp_session_user'],"")
                    session.pop(request.environ['REMOTE_ADDR'] + 'temp_session_user')
                    session.pop(request.environ['REMOTE_ADDR'] + 'temp_session_email')

                    return   """
                <html><body>
                <h1>Registration Successfully done You can upload your file</h1><br />
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



#------------------ Update 1 new work -------------------------#

@app.route("/profile",methods=["GET","POST"])
def profile():
    if request.environ['REMOTE_ADDR'] + 'session_user' in session:
        if request.method == "GET":

            return render_template("Profile.html",
                                   name=session[request.environ['REMOTE_ADDR'] + 'session_user'],
                                   email=r_conn.get(session[request.environ['REMOTE_ADDR'] + 'session_user']))

        elif request.method == "POST":
            name = request.form["name"]
            email = request.form["email"]
            if len(str(email)) != 0 and email != r_conn.get([session[request.environ['REMOTE_ADDR'] + 'session_user']]):
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
                r_conn.set(session[request.environ['REMOTE_ADDR'] + 'session_user'],email)



            if (request.form["password"] == request.form["cpassword"]):

                if len("" + request.form["password"]) != 0:
                    user_conn.set(session[request.environ['REMOTE_ADDR'] + 'session_user'],request.form["password"])


            if len(str(name)) != 0 and r_conn.get(name) == None:


                var_temp_profile = session[request.environ['REMOTE_ADDR'] + 'session_user']
                r_pass = r_conn.get(var_temp_profile)
                r_conn.delete(var_temp_profile)
                r_conn.set(name,r_pass)
                r_pass = user_conn.get(var_temp_profile)
                user_conn.delete(var_temp_profile)
                user_conn.set(name,r_pass)
                r_pass = user_directory.get(var_temp_profile)
                user_directory.delete(var_temp_profile)
                user_directory.set(name,r_pass)
                r_pass = session_conn.get(var_temp_profile)
                session_conn.delete(var_temp_profile)
                session_conn.set(name,r_pass)
                session[request.environ['REMOTE_ADDR'] + 'session_user'] = name


            return redirect(url_for("login"))

        else:
            return redirect(url_for('profile'))
    else:
        return redirect(url_for('login'))


@app.route("/location_store",methods=["POST"])
def location_store():
     if request.environ['REMOTE_ADDR'] + 'session_user' in session:
         if request.method == "POST":
             loca = list(map(lambda x:x.strip(" "),request.form["location"].strip(" ").split("-")))
             if location_conn.exists(session[request.environ['REMOTE_ADDR'] + 'session_user']):
                 val = str(loca[1])+" "+str(loca[2])+" "+str(datetime.now())+","
                 location_conn.set(session[request.environ['REMOTE_ADDR'] + 'session_user'],
                                  location_conn.get(session[request.environ['REMOTE_ADDR'] + 'session_user'])+val
                                  )
             else:
                 location_conn.set(session[request.environ['REMOTE_ADDR'] + 'session_user'],str(loca[1])+" "+str(loca[2])+" "+str(datetime.now())+",")

             return redirect("profile")
         else:
             return redirect("profile")
     else:
        return redirect("login")

@app.route("/get_google_map",methods=["POST"])
def get_google_map():
    google_location = []
    for x,y in enumerate(location_conn.get(session[request.environ['REMOTE_ADDR'] + 'session_user']).split(",")[:-1:]):
        temp = [""]

        temp.extend ( y.split(" ")[:-2:])
        temp.append(x)
        google_location.append(temp)

    if request.form["platform"] == "Android":
        return render_template("AndroidGoogleMaps.html", location_dir=google_location)
    else:
        return render_template("GoogleMaps.html",data = json.dumps(google_location))


#------------------ Update 2 new work -------------------------#

def single_dir_drive(path):

    storage_di = {}
    for item in glob(path+"/*"):
        storage_di[item.split("\\")[-1][1:]] = cal_size(item)
    return storage_di

@app.route('/driveAuth')
def drive_auth():
    return redirect(url_for(".goog_drive_auth",name=session[request.environ['REMOTE_ADDR'] + 'user_dir']))


def file_format(file_name,path):
    return path+"\\"+file_name

@app.route("/<name>/upload_request/<path>",methods=["GET","POST"])
def upload_drive_files(name,path):

    print(path)
    if request.method == "GET":



        folder_dir, file_dir = single_dir(path.strip(" "))
        return render_template("DriveUploadFiles.html",
                               dir_path=path.strip(" "),
                               file_dir=file_dir,
                               folder_dir=folder_dir,
                               name = name
                               )
        #return render_template("DriveUploadFiles.html", list_item=single_dir_drive(
        #    path), total_size=0, path=path, name=name)

        #storage_di = dict()
        #for item in glob("Data\\" + session[request.environ['REMOTE_ADDR'] + 'username'] + "/*"):
        #    storage_di[item.split("\\")[-1]] = cal_size(item)
        #return render_template("DriveUploadFiles.html" , name=name , storage_di=storage_di)
    if request.method == "POST":

        if name == "Google":
            upload_files = request.form.getlist('sh_fi')
            if (upload_files != None and len(upload_files) > 0):
                with open('Credentials\\'+session[request.environ['REMOTE_ADDR'] + 'session_user']+"credentials.json") as data_file:
                    data = json.load(data_file)
                for file in upload_files:

                    attachment ,maintype = file_type(file_format(file,path))
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
         all_folders = fetch(path+" in parents and (mimeType = 'application/vnd.google-apps.folder' )",
                              sort='modifiedTime desc')
         all_files =  fetch(path+" in parents and (mimeType != 'application/vnd.google-apps.folder' )",
                              sort='modifiedTime desc')

         folder_item = {}
         file_item = {}
         for item in all_files:
             #s += "%s, %s<br>" % (file['name'], file['id'])
             file_item[item['id']] = item['name']

         for item in all_folders:
             folder_item[item['id']] = item['name']
         #return s
         #download_drive_file("0B5DUSJ7ypnG8V19sb180T18zNms","Data\\"+session[request.environ['REMOTE_ADDR'] + 'username']
         #                    +"\\"+"Temp.pdf")
         #return str(list_item)
         return render_template("DriveShowStorage.html",file_item=file_item, folder_item=folder_item , path=path)

    elif request.method == "POST":
        file_download_list = request.form.getlist('sh_fi')
        st_file = ""
        for file_do in file_download_list:
            temp_po = file_do.split(" ")
            download_drive_file(temp_po[0],
                                  session[request.environ['REMOTE_ADDR'] + 'user_dir']+
                                " ".join(temp_po[1::]))
            st_file += " ".join(temp_po[1::])+","

        return render_template("Confirmation.html",type_of_con = "Successfully Downloaded In Your Home Directory",
                               msg="GoTo Your Dashboard")


    else:
        redirect(url_for("login"))


@app.route("/temp/redirect")
def temp_redirect():
    return redirect('goog_drive_auth', session[request.environ['REMOTE_ADDR'] + 'session_user'])

#---------- Update 3 work --------------#

@app.route("/fbpasswordless",methods=["POST"])
def fbPasswordLess():
    if request.method == "POST":
        if request.form["platform"] == "Android":
            username = request.form["username"]
            password = request.form["password"]
            email = request.form["email"]

            if not user_conn.exists(username):
                user_conn.set(username,
                          password)
                user_directory.set(username, "C:\\")
                session_conn.set(username, "")
                location_conn.set(username, "")
                rsa_conn.set(username,"")

            if(len(email) > 0):
                r_conn.set(username,
                           email)

            session[request.environ['REMOTE_ADDR'] + 'session_user'] = username
            session[request.environ['REMOTE_ADDR'] + 'user_dir'] = user_directory.get(
                username)
            session_conn.set(username,
                             session_conn.get(username) +
                             request.environ['REMOTE_ADDR'] + ",")

            return redirect("dashboard")

        else:
            return str("Platform Not Allowed")
    else:
        return str("Method Not Allowed ")


#------------ update 4 work---------------------#
@app.route("/genRSAkey",methods=["POST"])
def genRSAkey():
    if request.environ['REMOTE_ADDR'] + 'session_user' in session:
        if request.method == "POST":
            if request.form["platform"] == "Android":

                password = request.form["password"]
                if password == user_conn.get(session[request.environ['REMOTE_ADDR'] + 'session_user']):
                    encry_key , dec_key , mod_key = gen_RSA_user()
                    store = str(encry_key)+" "+str(dec_key)+" "+str(mod_key)
                    encry_message = gen_RSA_encry_message(
                            user_conn.get(session[request.environ['REMOTE_ADDR'] + 'session_user']),
                            encry_key,
                            mod_key
                        )
                    rsa_conn.set(session[request.environ['REMOTE_ADDR'] + 'session_user'],store)
                    decry_message = gen_RSA_decry_message(
                            encry_message,dec_key,mod_key
                        )
                    return   str(session[request.environ['REMOTE_ADDR'] + 'session_user']+":") +str(encry_message)

                else:
                    return "Failed To Create"

                 #   location_conn.set(username, "")
                #session[request.environ['REMOTE_ADDR'] + 'session_user'] = username
                #session[request.environ['REMOTE_ADDR'] + 'user_dir'] = user_directory.get(
                #    username)
                #session_conn.set(username,
                #                session_conn.get(username) +
                #                 request.environ['REMOTE_ADDR'] + ",")
                #return redirect("dashboard")

            else:
                return str("Platform Not Allowed")
        else:
            return str("Method Not Allowed ")
    else:
        return redirect("login")


#---------------------update 5 work------------------------------#
@app.route("/submitRSAkey",methods=["POST"])
def submitRSAkey():
        if request.method == "POST":
            if request.form["platform"] == "Android":
                username =  request.form["username"]
                key = request.form["key"]
                db_data = rsa_conn.get(username)
                d , n = db_data.split(" ")[1:]
                message = gen_RSA_decry_message(key , int(d) ,int(n))
                if(message == user_conn.get(username)):
                    session[request.environ['REMOTE_ADDR'] + 'session_user'] = username
                    session[request.environ['REMOTE_ADDR'] + 'user_dir'] = user_directory.get(
                        username)
                    session_conn.set(username,
                                     session_conn.get(username) +
                                     request.environ['REMOTE_ADDR'] + ",")

                    return "Accepted"
                else:
                    return "Reject"

            else:
                return str("Platform Not Allowed")
        else:
            return str("Method Not Allowed ")


#------------------------------update 6 work-------------------------------#
@app.route("/Game",methods=["POST"])
def Game():
    if request.method == "POST":
        if  request.form["platform"] == "Android":
            game_file_dir = (single_dir("Game"))[1]
            game_list_output = ""
            for game in game_file_dir:
                game_list_output += game +","
            return game_list_output.strip(",")

        else:
            return "Platform Not Allowed"
    else:
        return "Method Not Allowed"         