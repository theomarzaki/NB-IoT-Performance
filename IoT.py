
# This file represents the AT command interface used to connect with the module
#import RPi.GPIO as GPIO #specific for Raspberry pi
import serial
import time
from logger import log
import os
import subprocess

class Module():
    def __init__(self,serial_dev,baud_rate):
        self.logger = log
        self.device = serial.Serial(serial_dev,baud_rate)
        self.device.flushInput()
        self.dial_number = '*99***1#;'
        self.username = "user"
        self.password = "password"

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
                return rec_buffer.decode().replace("\n","")
        except Exception as e:
            self.logger.exception("Could not send to module")
            if self.device != None:
                self.device.close()
            else:
                self.logger.error("no device connected")

    def SetUpConnection(self):
        # dial_command = "ATD" + self.dial_number #check response is CONNECT
        # init_1 = "ATZ" #check response is OK
        # init_2 = ""
        #
        # #init modem configs
        # response = self.Command(init_1)
        # assert("OK" in response)
        # #set up dial connection
        # response = self.Command(dial_command)
        # assert("CONNECT" in response)
        subprocess("wvdial")

        #obtain the ip addresses

        #check that command can still be sent
