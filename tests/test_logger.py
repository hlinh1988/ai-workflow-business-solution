from app.logger import get_logger
import os

def test_logger():
    logger = get_logger()
    logger.info('Logger test message')
    assert os.path.exists('logs/app.log')
