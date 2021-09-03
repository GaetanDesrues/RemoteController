FROM python:3.8-slim

ARG USER_NAME=cntrllr
RUN useradd -ms /bin/bash $USER_NAME
USER $USER_NAME
WORKDIR /home/$USER_NAME/app
ADD . /home/$USER_NAME/app

RUN pip install --upgrade --user pip && pip install --user -r requirements.txt

CMD ["python", "start.py"]
