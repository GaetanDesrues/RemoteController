import argparse
import logging
import time

import socketio
import treefiles as tf
from pyPS4Controller.controller import Controller

sio = socketio.Client()


@sio.event
def connect():
    log.info("connection established")

    class MyController(Controller):
        def __init__(self, interface):
            super().__init__(interface)
            # self.cont = True

        # def start_continous(self, values):
        #     while self.cont:
        #         sio.emit("updt", values)
        #         time.sleep(1)

        # def on_x_release(self):
        #     sio.emit("updt", {"x": 5, "y": 0})

        def on_L3_down(self, v):
            d = {"x": 0, "y": v * 1e-3}
            sio.emit("updt", d)
            # self.start_continous(d)

        def on_L3_up(self, v):
            d = {"x": 0, "y": v * 1e-3}
            sio.emit("updt", d)
            # self.start_continous(d)

        def on_L3_left(self, v):
            d = {"x": v * 1e-3, "y": 0}
            sio.emit("updt", d)
            # self.start_continous(d)

        def on_L3_right(self, v):
            d = {"x": v * 1e-3, "y": 0}
            sio.emit("updt", d)
            # self.start_continous(d)

        # def on_L3_x_at_rest(self):
        #     self.cont = False
        #
        # def on_L3_y_at_rest(self):
        #     self.cont = False

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
