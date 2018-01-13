from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from __init__ import app

@app.route("/",methods=["GET"])
def home():
    return render_template("welcome.html")+"""
    <a href='"""+url_for("create")+"""'>enter my page</a></body></html>"""

@app.route("/create",methods=["GET","POST"])
def create():
    if request.method == "GET":
        return render_template("AddQuestions.html")
    elif request.method == "POST":
        question = request.form["question"]
        answer = request.form["answer"]
        return render_template("SaveQuestions.html",question=question,answer=answer)
    else:
        return render_template("PageError.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("PageError.html"),404