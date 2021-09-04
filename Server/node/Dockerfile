FROM node


ARG USER_NAME=cntrllr
RUN useradd -ms /bin/bash $USER_NAME
WORKDIR /home/$USER_NAME/app

RUN npm install express@4 socket.io

USER $USER_NAME
ADD . /home/$USER_NAME/app

EXPOSE 5011:5011

CMD ["node", "project/server.js"]
