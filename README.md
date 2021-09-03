# Client side RemoteController

## Install

### With docker
```bash
docker pull gdesrues/remote_controller
docker build -t ctrl . && docker run --rm --device /dev/input/js1 ctrl
```

### From sources
```bash
git clone git@github.com:GaetanDesrues/RemoteController.git
cd RemoteController
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python start.py
```
