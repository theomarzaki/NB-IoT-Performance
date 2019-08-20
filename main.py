from IoT import Module
from GA import GA
from utils import Evolve
from logger import log
from network_interface import Listener,Sender
import getopt,sys,configparser
import os

SENDER = '-s'
RECEIVER = '-r'

def main(argv):
    # obtaining confiurations
    config = configparser.ConfigParser()
    config.read('config.ini')
    # obtain command line arguments. Sender --> Module sending TCP packets , Receiver --> server to recieve TCP packets sent from module
    opts, args = getopt.getopt(argv,"sr",["sender","receiver"])


    for opt, arg in opts:
        if opt == SENDER:

            # client = Sender(config.get('Sender','address'),int(config.get('Sender','port')))
            # client.send()



            #set device based on configurations
            module = Module(config.get('Module','device'),int(config.get('Module','baud_rate')))
            # set up p2p connection on modem
            module.SetUpConnection() # os.system("wvdial")

            while True:
                cmd = input("Command: ")
                module.Command(cmd)


        elif opt == RECEIVER:

            # listener to recieve data from the module
            server = Listener(config.get('Receiver','address'),int(config.get('Receiver','port')))
            server.listen()

        else:
            sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])
