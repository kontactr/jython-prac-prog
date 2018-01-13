from flask import Flask

app = Flask(__name__)
wsgi_app = app.wsgi_app
from routes import *

if __name__ == "__main__":
    app.run()