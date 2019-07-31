#import RPi.GPIO as GPIO #specific for Raspberry pi
import serial
import time
from logger import log
import sys

class IoT():
    def __init__(self,serial_dev,baud_rate):
        self.logger = log
        self.device = serial.Serial(serial_dev,baud_rate)
        self.device.flushInput()

    def Command(self,command):
        try:
            rec_buffer = ''
            self.device.write((command + '\r\n').encode())
            time.sleep(0.1)
            if self.device.inWaiting():
                time.sleep(0.1)
                rec_buffer = self.device.read(self.device.inWaiting())
            if rec_buffer != '':
                print(rec_buffer.decode()) #debugging purposes
                self.logger.debug(command + " : " + rec_buffer.decode())
                rec_buffer = ''
        except Exception as e:
            self.logger.exception("Could not send to module")
            if self.device != None:
                self.device.close()
            else:
                self.logger.error("no device connected")

def main():
    IoT("/dev/ttyACM1",115200).Command(str(sys.argv[1]))

if __name__ == "__main__":
    main()
