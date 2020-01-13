FROM debian:buster

RUN apt-get update

RUN apt-get install -y build-essential net-tools ppp vim python3 python3-pip rsyslog

COPY . /communication_layer

WORKDIR /communication_layer

RUN pip3 install -r configuration/requirements.txt

RUN mv configuration/ppp_options /etc/ppp/options

RUN mv configuration/ppp_chat_isp /etc/ppp/chat-isp
