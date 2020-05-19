"""
logger.py \n

Logging operations.
"""

import logging


class AppLogger:
    """
        Class to perform logging operations for info and error logs.
        Parameters
        ----------
            filename
                the file to log information
    """

    def __init__(self):
        logging.basicConfig(
            filename='app.log',
            level=logging.INFO,
            filemode='w',
            format='%(asctime)s %(levelname)s %(message)s')

        self.logger = logging.getLogger()

    def log_info(self, message):
        """
            Log messages to the app.log file with INFO level.
            Parameters
            ----------
                message
                    message string to log
        """
        self.logger.info(message)

    def log_error(self, message):
        """
            Log messages to the app.log file with ERROR level. If used in an "except" block it will log the whole
            stack trace error.
            Parameters
            ----------
                message
                    message string to log
        """
        self.logger.error(msg=message, exc_info=True)
