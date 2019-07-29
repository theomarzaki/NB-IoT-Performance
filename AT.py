import RPi.GPIO as GPIO #specific for Raspberry pi
import serial
import time
import logging

class IoT():
    def __init__(self,serial_dev,baud_rate):
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
                logging.debug(rec_buffer.decode())
                rec_buffer = ''
        except Exception as e:
            logging.exception("Could not send to module")
            if self.device != None:
                self.device.close()
            else:

                logging.error("no device connected")

def main():
    logging.basicConfig(filename='logs/module.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
    IoT("/dev/ttyAMA0",9600).Command("AT")

if __name__ == "__main__":
    main()
