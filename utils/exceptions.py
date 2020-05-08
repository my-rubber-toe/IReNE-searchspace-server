import datetime
from utils.logger import AppLogger


class SearchSpaceError(Exception):
    """Base Audit Manager Error Class"""
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
        log_string = '"error":"{}","error_type":"{}","user":"{}","log_action":"{}",' \
                     '"error_description":"{}","status":"{}", "time_stamp": "{}"'.format(
            str(self.err).replace('"', "'"),
            str(self.error_type).replace('"', "'"),
            str(self.user),
            str(self.action).replace('"', "'"),
            str(self.error_stack),
            str(self.status),
            str(self.now.strftime("%a, %d %b %Y %I:%M:%S %p"))
        )

        log_string = '{' + log_string + '},\n'
        self.logger.log_error(log_string)

    def __str__(self):
        return f'\nApplication is in DEBUG MODE:\nError Pretty Print:\n\tType:{self.error_type}; Msg:{self.msg}; Status:{self.status}; ' \
               f'ErrStackTrace:{self.error_stack}'


class SearchSpaceApiError(SearchSpaceError):
    """Audit Manager API error"""
    error_type = 'SearchSpace Api Error'


class SearchSpaceRequestValidationError(SearchSpaceError):
    """Audit Manager API error"""
    error_type = 'SearchSpace Request Validation Error'


class SearchSpaceRequestError(SearchSpaceError):
    """Audit Manager API error"""
    error_type = 'SearchSpace Request Error'
