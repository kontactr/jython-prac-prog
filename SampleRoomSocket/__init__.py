from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

app = Flask(__name__)
app.config['SECRET_KEY'] = "Secret!"
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message',namespace='/test')
def send_message(message):
    emit('my_response',{'data':message['data']},room='location')

@socketio.on('connect',namespace='/test')
def connection():
    join_room('location')
    emit('my_response',{'data':'room-location'})

@socketio.on('disconnect_req',namespace='/test')
def disconnect_req():
    leave_room('location')
    print ("Called")
    emit('my_response',{'data':'Disconnected'})
    disconnect()

if __name__ == '__main__':
    socketio.run(app, debug=True , host="0.0.0.0")
