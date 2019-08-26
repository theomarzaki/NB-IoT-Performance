FROM debian:buster

RUN apt-get update

RUN apt-get install -y build-essential ppp vim python3 python3-pip

COPY . /communication_layer

COPY ./configuration/ppp_options /etc/ppp

COPY ./configuration/ppp_chat_isp /etc/ppp

COPY /etc/ppp/ppp_chat_isp /etc/ppp/chat-isp

COPY /etc/ppp/ppp_options /etc/ppp/options

WORKDIR /communication_layer

RUN pip3 install -r requirements.txt
