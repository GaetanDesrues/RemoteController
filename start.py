import getpass
import logging

import treefiles as tf


@tf.timer
def main():
    log.info(f"Seems to be working so far, btw I am {getpass.getuser()}")


log = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    log = tf.get_logger()

    main()
