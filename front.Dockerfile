FROM ubuntu:20.04

RUN apt update -y && apt upgrade -y && apt install -y gnupg2

ENV DEBIAN_FRONTEND=noninteractive

RUN apt install nodejs npm -y

COPY ./frontend /frontend

EXPOSE 3000/tcp

WORKDIR /frontend

RUN npm install

ENTRYPOINT ["npm", "start"]
