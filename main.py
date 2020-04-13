from IoT import Module, DialUpThread
from logger import log, passive_log
from network_interface import Listener,Sender
import getopt,sys,configparser
import os
import time
import threading
import subprocess
import torch
from Config import Config
import argparse
from utils import takeAction
import joblib
import numpy as np
from utils import getFeatures

def main(argv):
    # obtaining confiurations
    config = configparser.ConfigParser()
    config.read('configuration/config.ini')

    parser = argparse.ArgumentParser(description="Configuration advocator")

    parser.add_argument("--dialup","--d", action='store_true',help='Set up a Peer-to-Peer (P2P) connection with host and device')
    parser.add_argument("--command","--c", action='store_true',help='Send specific commands from host to device')
    parser.add_argument("--log","--l", action='store_true',help='Enter passive logging mode of the device')
    parser.add_argument("--suggest","--s", action='store_true',help='Suggest configuration for device')
    parser.add_argument("--delay","--ms", action='store_true', help='Use delay as metric for confiuration suggestion')
    parser.add_argument("--energy_consumption","--ec", action='store_true',help='Use energy consumption as metric for confiuration suggestion')
    parser.add_argument("--combination","--all", action='store_true',help='Use combination of metrics for confiuration suggestion')

    args = parser.parse_args()

    threadLock = threading.Lock() #allows synchronoisty of the modem dial up and main communication

    # module = Module(config.get('Module','device'),int(config.get('Module','baud_rate')))

    model = None
    module = None

    scaler = joblib.load('Models/label_enc_no_tx.save')

    if args.delay:
        model = torch.jit.load('Models/GD_model_no_tx_ms.pt')

    elif args.energy_consumption:
        model = torch.jit.load('Models/GD_model_no_tx_ec.pt')

    elif args.combination:
        model = torch.jit.load('Models/GD_model_no_tx_all.pt')
    else:
        pass

    if args.log:
        log_thread = threading.Thread(target = passive_log(config.get('Module','device')))
        log_thread.start()

    if args.dialup:
        DialUpThread(threadLock,module).start()
        time.sleep(10)
        if(subprocess.check_output("ifconfig | grep ppp0",shell=True) == ""):
            log.error("Could not initiate interface")
        else:
            log.debug("Interface is up and running")

    elif args.command:
        while True:
            module.Command(input('Execute Command: '))

    elif args.suggest:

        configuration = torch.Tensor(getFeatures(module))

        config = torch.Tensor(Config(scaler,configuration).get_scaled_paramaters())

        action_tensor = torch.zeros(5)

        action_tensor[torch.argmax(model(config)).item()] = 1
        takeAction(action_tensor,module)

    else:
        sys.exit()

if __name__ == '__main__':
    main(sys.argv[1:])
