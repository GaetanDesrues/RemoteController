#!/bin/bash

# Current dirname
ROOT="$(dirname "$(realpath $0)")"

# Docker image name
IMG=gdesrues/remote_controller

# Build image
docker build -t $IMG:server_node $ROOT

# Send to docker hub
docker push $IMG:server_node