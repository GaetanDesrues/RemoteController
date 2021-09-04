#!/bin/bash

docker build -t my_node_app .
docker run --rm --network="host" --init my_node_app
#docker run -it --rm --network="host" my_node_app bash