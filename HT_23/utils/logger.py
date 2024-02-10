"""
Module for configuring a rotating file logger.
This module defines a logger with the following configuration:
    - Logger name: __name__
    - Log level: ERROR
    - Log messages are written to a rotating file 'logs/error.log' with
      a maximum size of 10 MB and 5 backup copies.
"""

import logging
from logging.handlers import RotatingFileHandler


# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

# Create a formatter Handler for writing to a file
handler = RotatingFileHandler('logs/error.log', maxBytes=10*1024*1024, backupCount=5)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add a handler to the logger
logger.addHandler(handler)
