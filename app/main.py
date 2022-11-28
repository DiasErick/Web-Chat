from flask import Flask, render_template
from flask_socketio import SocketIO, send

#Creating app Flask
app = Flask(__name__)

#Autorizing all origins
socketio = SocketIO(app, cors_allowed_origins="*")

#Haandling received messages
@socketio.on('message')
def handle_message(message: str):    
    #Just sending the received messagem 
    if message != "User connected!":
        send(message, broadcast=True)

@app.route('/')
def index():
    #Rendering the index page
    return render_template("index.html")

if __name__ == '__main__':
    socketio.run(app, host="192.168.2.17")#Defining the ip address of server.