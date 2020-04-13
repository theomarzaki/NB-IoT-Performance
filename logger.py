#Logging functionality, that creates a file and saves the interaction between the device and user AT commands

import logging
import serial
import datetime
import sys
import os



logging.basicConfig(filename='module.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s',level=logging.DEBUG)
log = logging.getLogger('Module_Logger')

max_file_size = 10000000 #10MB
logfilename = "PLACEHOLDER"

def create_file():
    global logfilename
    time = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    logfilename = "debuglog_"+str(time)+".bin"
    fileobj = open(logfilename, "w+")
    return fileobj

def passive_log(module):
    try:
        #gets device logging channgel from the serial port connected to the host
        serialport = serial.Serial(module, 921600, timeout=0.1)
        if (serialport.isOpen() == False):
            print('Failed to open Serial Port.')
            exit()

        fileobj = create_file()

        while True:
            #reads output from the host, based on the AT command
            command = serialport.readline()
            if str(command):
                fileobj.write(str(command))
            if(os.stat(logfilename).st_size > max_file_size):
                fileobj.close()
                fileobj = create_file()

    except KeyboardInterrupt:
        print('interrupt received, stopping…')
    finally:
        serialport.close()
        fileobj.close();
