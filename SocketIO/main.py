import asyncio
import logging

import socketio
import treefiles as tf

sio = socketio.AsyncClient()


@sio.event
async def connect():
    log.info("connection established")

    # await emit({"x": 2, "y": 0})
    for i in range(5000):
        await emit({"x": 3, "y": 0})


@sio.event
async def disconnect():
    log.info("disconnected from server")


# @tf.debug
async def emit(msg):
    log.debug(f"Emitting message: {msg}")
    await sio.emit("updt", {"msg": msg})


async def main():
    # await sio.connect("https://loc.kerga.ga")
    await sio.connect("http://127.0.0.1:5011")
    await sio.wait()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("asyncio").setLevel(logging.INFO)
    log = tf.get_logger()

    asyncio.run(main())
