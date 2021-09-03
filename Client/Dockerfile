FROM python:3.8-slim

ARG USER_NAME=cntrllr
RUN useradd -ms /bin/bash $USER_NAME
USER $USER_NAME
WORKDIR /home/$USER_NAME/app
ADD . /home/$USER_NAME/app

RUN pip install --upgrade --user pip && pip install --user -r requirements.txt

EXPOSE 5005:5005
ENV REM_IP="127.0.0.1"
ENV REM_PORT=5005

ENTRYPOINT ["python", "start.py"]
