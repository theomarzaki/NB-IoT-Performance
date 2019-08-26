FROM debian:buster

RUN apt-get update

RUN apt-get install -y build-essential ppp vim python3 python3-pip

COPY . /communication_layer

WORKDIR /communication_layer

RUN pip3 install -r configuration/requirements.txt

CMD["sh configuration/init.sh"]
