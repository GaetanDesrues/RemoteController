#!/bin/bash

# Current dirname
ROOT="$(dirname "$(realpath $0)")/.."

# Docker image name
IMG=gdesrues/remote_controller

# Build image
docker build -t $IMG $ROOT/Client

## Send to docker hub
#docker push $IMG:latest