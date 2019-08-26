docker build -t iot .

docker run --privileged --device=/dev/ttyUSB0 -it iot bash
