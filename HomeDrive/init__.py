from flask import Flask


app = Flask(__name__)
app.secret_key = "home_drive"



from route import *


if __name__ == "__main__":
    app.run("0.0.0.0",5050,debug=True,threaded=True,ssl_context='adhoc')
