"""
exceptions.py \n
Handles the errors occurred.
"""

import datetime
from utils.logger import AppLogger


class SearchSpaceError( Exception):
    """
    Main class that handles the errors occurred.
    """
    error_type = 'SearchSpace Error'

    def __init__(self, err=None, msg='Error', status=500, user='', action=None):
        self.logger = AppLogger()
        self.msg = msg
        self.status = status
        if err:
            self.error_stack = [str(x).replace('"', "'") for x in err.args]
        else:
            self.error_stack = []
        self.error_stack.append(msg)
        self.err = err
        self.user = user
        self.action = action
        self.status = status
        self.now = datetime.datetime.now()
        self.log()

    def log(self):
        """
             Logs the errors using the AppLogger.

        """
        log_string = '"error":"{}","error_type":"{}"' \
                     '"error_description":"{}","status":"{}", "time_stamp": "{}"'.format(
            str(self.err).replace('"', "'"),
            str(self.error_type).replace('"', "'"),
            str(self.error_stack),
            str(self.status),
            str(self.now.strftime("%a, %d %b %Y %I:%M:%S %p"))
        )

        log_string = '{' + log_string + '},\n'
        self.logger.log_error(log_string)

    def __str__(self):
        """
        Turns the error object into a string.

        Returns
        -------
        string
            String representing the error object.
        """
        return f'\nApplication is in DEBUG MODE:\nError Pretty Print:\n\tType:{self.error_type}; Msg:{self.msg}; Status:{self.status}; ' \
               f'ErrStackTrace:{self.error_stack}'


class SearchSpaceApiError(SearchSpaceError):
    """Class for errors occurred during runtime of the server"""
    error_type = 'SearchSpace Api Error'


class SearchSpaceRequestValidationError(SearchSpaceError):
    """Class for errors occurred because a Validation error"""
    error_type = 'SearchSpace Request Validation Error'


class SearchSpaceRequestError(SearchSpaceError):
    """Class for errors occurred because a bad request error"""
    error_type = 'SearchSpace Request Error'
