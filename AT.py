import RPi.GPIO as GPIO #specific for Raspberry pi
import serial
import time


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
                print(rec_buffer.decode())
                rec_buffer = ''
        except Exception as e:
            print(e)
            if self.device != None:
                self.device.close()
            else:
                print("no device connected")


def main():
    IoT("/dev/ttyAMA0",9600).Command("AT")

if __name__ == "__main__":
    main()
