import logging

logging.basicConfig(filename='logs.txt', encoding='utf-8', format='%(asctime)s %(message)s', 
                    datefmt='%d/%m/%Y %H:%M:%S %a', level=logging.INFO)
log = logging.getLogger(__name__)

log.info('Initializing Folder Synchronizer')



