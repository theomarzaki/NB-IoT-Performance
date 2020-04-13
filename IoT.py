# This file represents the AT command interface used to connect with the module
#import RPi.GPIO as GPIO #specific for Raspberry pi
import serial
import time
from logger import log
import threading
import subprocess

#Module class that holds logging, command and dialup functionality
class Module():
    def __init__(self,serial_dev,baud_rate):
        self.logger = log
        self.device = serial.Serial(serial_dev,baud_rate)
        self.device.flushInput()

    #Function that allows the sending of commands from host to device
    def Command(self,command):
        try:
            rec_buffer = ''
            self.device.write((command + '\r\n').encode())
            time.sleep(0.1)
            #checks if device is ready to use, or is currently being used
            if self.device.inWaiting():
                time.sleep(1)
                rec_buffer = self.device.read(self.device.inWaiting())
            if rec_buffer != '':
                print(rec_buffer.decode()) #debugging purposes
                #logs command and response into logger
                self.logger.debug(command + " : " + rec_buffer.decode())
                return rec_buffer.decode().replace("\n","")
        # errors may stem from incorrect configurations on the device connected, or device is not connected/timed out
        except Exception as e:
            self.logger.exception("Could not send to module")
            if self.device != None:
                self.device.close()
            else:
                self.logger.error("No device connected")

    #calls up a bash file that sets up the dial up connection on the host to set up a p2p connection between device and host for ease of configuration suggestion
    def SetUpConnection(self):
        self.logger.debug("dialing")
        subprocess.check_output("sh init.sh",shell=True)

#allow the dial up connection to happen in parallel as the device connects, for a quicker and robust interaction with device. May have more than one p2p connection at the same time
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
