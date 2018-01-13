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



user_conn = redis.StrictRedis(db=14, charset="utf-8", decode_responses=True)

session_conn = redis.StrictRedis(db=15, charset="utf-8", decode_responses=True)


@app.route("/")
def home():
    return redirect("login")


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
            with open("Config","r") as file_name:
                session[request.environ['REMOTE_ADDR'] + 'user_dir'] = "".join((file_name.readline().split("=")[1:])).strip(" ")[:-1]
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
        if (compress_type.strip(" ") == "Deep Compress"):

            if select_list != None and len(select_list) > 0 :
                folder_list = []
                main_dict = {path:[]}
                for item in select_list:
                    if  check_folder(path+"\\"+item):
                        main_dict.update(round_fun(path+"\\"+item,{path+"\\"+item:[]}))
                    main_dict[path].append(path+"\\"+item)

                zip_file = "-".join(str( datetime.now().time() ).split(":")[:3])+".zip"
                remove_dir = [os.path.join(".", zip_file)]

                myZipFile = zipfile.ZipFile(zip_file,"w",zipfile.ZIP_DEFLATED)
                make_zip(path,myZipFile,main_dict,remove_dir)
                myZipFile.close()
                myThread(remove_dir).start()
                return send_file(os.path.join(".", zip_file),as_attachment=True)
                #return redirect(url_for("view_data",path=path))

            else:
                    return redirect(url_for("view_data",path=path))

        else:
            if select_list != None and len(select_list) > 0 :
                got_tar_file = str(build_tar_file(path,select_list))
                myThread([got_tar_file]).start()
                return send_file(os.path.join(".", got_tar_file),as_attachment=True)
            else:
                return redirect(url_for("view_data",path=path))
    else:
        return redirect("login")




@app.route("/Config",methods=["GET","POST"])
def config_data():
    if request.method == "GET":
        return render_template("Settings.html")

    elif request.method == "POST":
        with open("Config","w") as filename:
            filename.write("Directory= "+request.form["Directory"])
        with open("Config","r") as file_name:
                session[request.environ['REMOTE_ADDR'] + 'user_dir'] = "".join((file_name.readline().split("=")[1:])).strip(" ")[:-1]
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
