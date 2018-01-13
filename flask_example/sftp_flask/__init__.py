from flask import Flask


app = Flask(__name__)
app.secret_key = "sftp_flask"



from route import *


if __name__ == "__main__":
    if os.path.exists('client_id.json') == False:
        print('Client secrets file (client_id.json) not found in the app path.')
    app.run(debug=True)

