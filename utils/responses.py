"""
responses.py \n
    Classes to standardize the response methods. Improves the ease of debugging.
"""

from flask import make_response, jsonify


class ApiResult(object):
    """
    API results response wrapper class
    """

    def __init__(self, status=200, **kwargs):
        self.res = jsonify(**kwargs)
        self.status = status

    def to_response(self):
        """
            Converts this class instance into a Flask Response object.
            Returns
            -------
                Response
                    a flask response instance with a response message and status.
        """
        return make_response(self.res, self.status)


class ApiException(object):
    """API exception response wrapper class"""
    def __init__(self, error_type='ApiError', message='Error', status=500):
        self.res = jsonify(error_type=error_type, message=message, status=status)
        self.status = status

    def to_response(self):
        """
            Converts this class instance into a Flask Response object.
            Returns
            -------
                Response
                    a flask response instance with a response message and status.
        """
        return make_response(self.res, self.status)

