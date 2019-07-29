import logging

logging.basicConfig(filename='module.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s',level=logging.DEBUG)
log = logging.getLogger('Module_Logger')
