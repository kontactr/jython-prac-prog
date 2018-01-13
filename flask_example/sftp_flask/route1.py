
from TempServer import app
import os
import urllib.request
from glob import glob

import redis
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename
import json
#from __init__ import app
from datetime import datetime
from decimal import *



@app.route("/",methods=["POST"])
def home():
        data = request.get_json()
        p = json.dumps({"A": 1, "B": 2})

        return str(p)


