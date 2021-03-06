from flask import Flask , render_template
from flask_socketio import  SocketIO , emit
from views import *
app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():

    return render_template('index.html')

@socketio.on('my event' , namespace='/test')
def test_message(message):
    print ('event')
    emit('my response' , {'data':message['data']})

@socketio.on('my broadcast event',namespace='/test')
def test_message(message):
    print ('hello-broadcast')
    emit('my response',{'data':message['data']},broadcast=True)

@socketio.on('connect',namespace='/test')
def test_connect():
    emit('my response',{'data':'Connected'})

@socketio.on('disconnect',namespace='/test')
def test_disconnect():
    print ('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)
