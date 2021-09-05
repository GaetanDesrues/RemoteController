# using eventlet, visit the docs for more info
import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(
    sio, static_files={"/": {"content_type": "text/html", "filename": "index.html"}}
)


@sio.event
def connect(sid, environ):
    print("connect ", sid)


@sio.event
def my_message(sid, data):
    print("message ", data)


@sio.event
def disconnect(sid):
    print("disconnect ", sid)


if __name__ == "__main__":
    # change the 5000 to any port you want
    # leave the 'localhost' empty string to run on your IP
    eventlet.wsgi.server(eventlet.listen(("localhost", 5000)), app)
