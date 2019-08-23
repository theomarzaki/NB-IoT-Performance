FROM debian:buster

RUN apt-get update

RUN apt-get install -y build-essential vim

COPY . /communication_layer

WORKDIR /communication_layer
