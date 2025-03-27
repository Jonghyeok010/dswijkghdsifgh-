
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import eventlet

eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

@app.route("/")
def index():
    return render_template("video_chat.html")

@socketio.on('offer')
def handle_offer(data):
    emit('offer', data, broadcast=True)

@socketio.on('answer')
def handle_answer(data):
    emit('answer', data, broadcast=True)

@socketio.on('candidate')
def handle_candidate(data):
    emit('candidate', data, broadcast=True)

@socketio.on('chat')
def handle_chat(data):
    emit('chat', data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
