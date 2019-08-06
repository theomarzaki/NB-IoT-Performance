from AT import IoT
from GA import GA
from utils import Evolve
from logger import log
from network_interface import Listener
import configparser


def main():
    # obtaining confiurations
    config = configparser.ConfigParser()
    config.read('config.ini')

    # set device based on configurations
    # module = IoT(config.get('Module','device'),int(config.get('Module','baud_rate')))

    # listener to recieve data from the module
    client_data = Listener(config.get('Network','address'),int(config.get('Network','port')))

    print("data: {}".format(client_data))



if __name__ == '__main__':
    main()
