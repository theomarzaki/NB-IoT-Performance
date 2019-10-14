from IoT import Module, DialUpThread
from GA import GA
from utils import Evolve
from logger import log
from network_interface import Listener,Sender
import getopt,sys,configparser
import os
import time
import threading
import subprocess

DIAL_MODE = '-d'
COMMAND_MODE = '-c'

def main(argv):
    # obtaining confiurations
    config = configparser.ConfigParser()
    config.read('configuration/config.ini')

    opts, args = getopt.getopt(argv,"dc",["dialup","command"])

    threadLock = threading.Lock() #allows synchronoisty of the modem dial up and main communication

    module = Module(config.get('Module','device'),int(config.get('Module','baud_rate')))

    for opt, arg in opts:
        if opt == DIAL_MODE:

            DialUpThread(threadLock,module).start()

            time.sleep(10)

            if(subprocess.check_output("ifconfig | grep ppp0",shell=True) == ""):
                log.error("Could not initiate interface")
            else:
                log.debug("Interface is up and running")

        elif opt == COMMAND_MODE:
            log_thread = threading.Thread(target = passive_log(), args =(config.get('Module','device'),))
            log_thread.start()
            while True:
                module.Command(input('Execute Command: '))

        else:
            sys.exit()



if __name__ == '__main__':
    main(sys.argv[1:])
