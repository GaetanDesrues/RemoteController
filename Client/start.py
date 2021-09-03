import argparse
import logging
import os
import socket

import treefiles as tf
from pyPS4Controller.controller import Controller


def start_client(device_path):
    credentials = os.environ["REM_IP"], int(os.environ["REM_PORT"])
    opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    send = lambda x: opened_socket.sendto(bytes(x, "utf-8"), credentials)

    class MyController(Controller):
        def on_x_release(self):
            send("X REL")

    controller = MyController(interface=device_path)
    controller.listen()


log = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    log = tf.get_logger()

    parser = argparse.ArgumentParser()
    parser.add_argument("device", type=str)
    args = parser.parse_args()

    start_client(args.device)
