import logging

# Creates a log when the program runs
def initialize_logger(log_file_path):
    logging.basicConfig(filename=log_file_path, encoding='utf-8', format='%(asctime)s %(message)s', 
                        datefmt='%d/%m/%Y %H:%M:%S %a', level=logging.INFO)
    
    log = logging.getLogger(__name__)
    log.info('Initializing Folder Synchronizer')

    return log
