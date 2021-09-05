#!/bin/bash

# Get last input event
INP="/dev/input/$(ls /dev/input | grep js | tail -n 1)"

# Docker image name
IMG=gdesrues/remote_controller

## Pull image from docker hub
#docker pull $IMG:latest

# Start client
docker run --rm -it --device $INP --network="host" $IMG $INP