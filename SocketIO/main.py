import asyncio
import logging

import socketio
import treefiles as tf

sio = socketio.AsyncClient()


@sio.event
async def connect():
    log.info("connection established")

    for i in range(300):
        await emit(f"Coucou {i}")


@sio.event
async def disconnect():
    log.info("disconnected from server")


# @tf.debug
async def emit(msg):
    log.debug(f"Emitting message: {msg}")
    await sio.emit("updt", {"msg": msg})


async def main():
    await sio.connect("http://127.0.0.1:5011")
    await sio.wait()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("asyncio").setLevel(logging.INFO)
    log = tf.get_logger()

    asyncio.run(main())
