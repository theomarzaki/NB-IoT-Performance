docker build -t IoT .

docker run --device=/dev/ttyUSB0 -it IoT
