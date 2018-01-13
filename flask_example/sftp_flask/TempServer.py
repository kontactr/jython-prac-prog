from flask import Flask



app = Flask(__name__)
app.secret_key = "sftp_flask"

from route1 import *

if __name__ == "__main__":
    app.run(debug=True)
