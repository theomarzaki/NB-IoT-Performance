# This file represents the AT command interface used to connect with the module
#import RPi.GPIO as GPIO #specific for Raspberry pi
import serial
import time
from logger import log
import threading
import subprocess

class Module():
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
                time.sleep(1)
                rec_buffer = self.device.read(self.device.inWaiting())
            if rec_buffer != '':
                print(rec_buffer.decode()) #debugging purposes
                self.logger.debug(command + " : " + rec_buffer.decode())
                return rec_buffer.decode().replace("\n","")
        except Exception as e:
            self.logger.exception("Could not send to module")
            if self.device != None:
                self.device.close()
            else:
                self.logger.error("No device connected")

    def SetUpConnection(self):
        self.logger.debug("dialing")
        subprocess.check_output("sh init.sh",shell=True)
        if(subprocess.check_output("ifconfig | grep ppp0",shell=True) == ""):
            self.logger.error("Could not initiate interface")
            return False
        else:
            self.logger.debug("Interface is up and running")
            return True


class DialUpThread(threading.Thread):
    def __init__(self,threadLock,module):
        threading.Thread.__init__(self)
        self.module = module
        self.threadLock = threadLock

    def run(self):
        self.threadLock.acquire()
        # modem specific dial up
        interface_up = self.module.SetUpConnection()

        self.threadLock.release()

        return interface_up
