#!/bin/bash

if [ ! -d "venv" ]; then
	python -m venv venv
	git clone git@github.com:GaetanDesrues/RemoteController.git

	source venv/bin/activate
	pip install -r requirements.txt
else
	cd RemoteController/Client
	source venv/bin/activate
fi

# Get last input event
INP="/dev/input/$(ls /dev/input | grep js | tail -n 1)"

python start.py $INP