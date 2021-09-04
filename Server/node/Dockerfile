FROM node

ARG USER_NAME=cntrllr
RUN useradd -ms /bin/bash $USER_NAME
USER $USER_NAME
WORKDIR /home/$USER_NAME/app
ADD . /home/$USER_NAME/app

EXPOSE 5011:5011

CMD ["node", "server.js"]
