import argparse
import logging

import socketio
import treefiles as tf
from pyPS4Controller.controller import Controller

sio = socketio.Client()


@sio.event
def connect():
    log.info("connection established")

    class MyController(Controller):
        def on_x_release(self):
            sio.emit("updt", {"x": 3, "y": 0})

    controller = MyController(interface=device_path)
    controller.listen()


def start_client():
    url = f"http://127.0.0.1:5011"

    log.info(f"connecting to {url}")
    sio.connect(url)


log = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    log = tf.get_logger()

    parser = argparse.ArgumentParser()
    parser.add_argument("device", type=str)
    args = parser.parse_args()
    device_path = args.device

    start_client()
