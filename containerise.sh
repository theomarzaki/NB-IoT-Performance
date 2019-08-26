docker build -t iot .

docker run --privileged --net=bridge --device=/dev/ttyUSB0 -it iot
