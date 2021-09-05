FROM python:3.8-slim

ARG USER_NAME=cntrllr
RUN useradd -ms /bin/bash $USER_NAME
WORKDIR /home/$USER_NAME/app

#USER $USER_NAME
#ADD . /home/$USER_NAME/app
#RUN pip install --upgrade --user pip && pip install --user -r requirements.txt

# DEBUG avoid reinstall on source change
USER $USER_NAME
ADD ./requirements.txt /home/$USER_NAME/app
RUN pip install --upgrade --user pip && pip install --user -r requirements.txt
ADD . /home/$USER_NAME/app

#ENV REM_IP="192.168.1.39"
#ENV REM_IP="127.0.0.1"
ENV REM_IP="0.0.0.0"
ENV REM_PORT=5011

EXPOSE 5011:5011
ENTRYPOINT ["python", "start.py"]
