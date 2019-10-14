from IoT import Module, DialUpThread
from GA import GA
from utils import Evolve
from logger import log
from network_interface import Listener,Sender
import getopt,sys,configparser
import os
import time
import threading

SENDER = '-s'
RECEIVER = '-r'

def main(argv):
    # obtaining confiurations
    config = configparser.ConfigParser()
    config.read('configuration/config.ini')
    # obtain command line arguments. Sender --> Module sending TCP packets , Receiver --> server to recieve TCP packets sent from module
    opts, args = getopt.getopt(argv,"sr",["sender","receiver"])

    threadLock = threading.Lock() #allows synchronoisty of the modem dial up and main communication

    for opt, arg in opts:
        if opt == SENDER:
            #set device based on configurations
            module = Module(config.get('Module','device'),int(config.get('Module','baud_rate')))

            DialUpThread(threadLock,module).start()

            # set up p2p connection on modem
            print("finished dial up on main method")

            # client = Sender(config.get('Sender','address'),int(config.get('Sender','port')))
            # client.send()


        elif opt == RECEIVER:

            # listener to recieve data from the module
            server = Listener(config.get('Receiver','address'),int(config.get('Receiver','port')))
            server.listen()

        else:
            sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])
