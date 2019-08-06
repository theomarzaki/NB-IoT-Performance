from AT import IoT
from GA import GA
from utils import Evolve
from logger import log
from network_interface import Listener
import getopt,sys,configparser



def main(argv):
    # obtaining confiurations
    config = configparser.ConfigParser()
    config.read('config.ini')
    # obtain command line arguments. Sender --> Module sending TCP packets , Receiver --> server to recieve TCP packets sent from module
    opts, args = getopt.getopt(argv,"sr",["sender","receiver"])


    for opt, arg in opts:
        if opt == '-s':


            server_data = Sender(config.get('Sender','address'),int(config.get('Sender','port')))


            # set device based on configurations
            # module = IoT(config.get('Module','device'),int(config.get('Module','baud_rate')))

        elif opt == '-r':



            # listener to recieve data from the module
            client_data = Listener(config.get('Receiver','address'),int(config.get('Receiver','port')))

            print("data: {}".format(client_data))

        else:
            sys.exit()




if __name__ == '__main__':
    main(sys.argv[1:])
