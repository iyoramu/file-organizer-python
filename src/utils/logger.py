import logging
from typing import Any

def setup_logger(name: str) -> logging.Logger:
    """Configure and return a logger"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger

class FileOrganizerLogger:
    def __init__(self):
        self.logger = setup_logger('file-organizer')

    def info(self, message: str, *args: Any) -> None:
        self.logger.info(message, *args)

    def warning(self, message: str, *args: Any) -> None:
        self.logger.warning(message, *args)

    def error(self, message: str, *args: Any) -> None:
        self.logger.error(message, *args)
