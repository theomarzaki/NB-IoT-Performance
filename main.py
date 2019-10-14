from IoT import Module, DialUpThread
from GA import GA
from utils import Evolve
from logger import log
from network_interface import Listener,Sender
import getopt,sys,configparser
import os
import time
import threading

def main(argv):
    # obtaining confiurations
    config = configparser.ConfigParser()
    config.read('configuration/config.ini')
    # obtain command line arguments. Sender --> Module sending TCP packets , Receiver --> server to recieve TCP packets sent from module

    threadLock = threading.Lock() #allows synchronoisty of the modem dial up and main communication

    module = Module(config.get('Module','device'),int(config.get('Module','baud_rate')))

    DialUpThread(threadLock,module).start()

    while True:
        module.Command(input('Execute Command: '))


if __name__ == '__main__':
    main(sys.argv[1:])
