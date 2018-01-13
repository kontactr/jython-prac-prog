from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from __init__ import app
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt
import numpy as np
import csv
import os

app.config['UPLOAD_FOLDER'] = 'uploads/'

file_holder = None

@app.route("/")
def home():
    return """<a href='"""+\
           url_for("upload")\
           +"""'>Upload your file here </a>"""

@app.route("/upload",methods=["GET","POST"])
def upload():
    if (request.method == "GET"):
        return render_template("UploadFile.html")
    elif (request.method == "POST"):
        file = request.files["file"]
        #return str(file)
        #file = open(file,"r")
        #return file.read()
        filename = secure_filename(file.filename)
        global file_holder
        file_holder = filename
        return str(file.content_length)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return """
            <html>
            <head>
                <title>Graph Page</title>
            </head>
            <body>
                <h1>Successfully saved</h1><br />
                <h2>Graphs: </h2>
                <h3><a href='"""+url_for("simple_graph",title="simple_graph")+"""'>Simple X-Y Graph</a><br />
                <h3><a href='"""+url_for("simple_graph",title="plot_graph")+"""'>Plot Graph</a><br />
            </body>
            </html>"""
    else:
        return "Invalid"

@app.route("/upload/<title>")
def simple_graph(title):
    if(title == "simple_graph"):
        file = open((os.path.join(app.config['UPLOAD_FOLDER'], file_holder)),"r")
        reader = csv.reader(file)
        st , x,  y = "" , [] , []
        for data in reader:
            x.append(eval(data[0]))
            y.append(eval(data[1]))
        plt.plot(x,y)
        plt.grid(True)
        plt.savefig("static/"+str(file_holder.split(".")[0])+".png")
    return render_template("ImageDisplay.html",name=str(file_holder.split(".")[0])+".png")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("ImageDisplay.html",name="404-snake.png"),404

