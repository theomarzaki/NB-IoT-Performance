from AT import IoT
from GA import GA
from utils import Evolve
from logger import log
import configparser


def main():
    # obtaining confiurations
    config = configparser.ConfigParser()
    config.read('config.ini')

    # set device based on configurations
    module = IoT(config.get('Module','device'),config.get('Module','baud_rate'))


    module.Command("AT")




if __name__ == '__main__':
    main()
