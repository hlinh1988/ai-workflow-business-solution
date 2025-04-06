import logging

def get_logger():
    logger = logging.getLogger('ai_app')
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler('logs/app.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
