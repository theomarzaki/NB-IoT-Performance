FROM debian:buster

RUN apt-get update

RUN apt-get install -y build-essential net-tools wvdial ppp vim python3 python3-pip rsyslog

COPY . /communication_layer

WORKDIR /communication_layer

RUN pip3 install -r configuration/requirements.txt

RUN service rsyslog start

RUN sh configuration/init.sh
