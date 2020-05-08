import inspect
import sys

from flask import Flask
from flask_cors import CORS
from werkzeug.utils import find_modules, import_string

from DAOs.init_db import register_database
from utils.exceptions import SearchSpaceApiError, SearchSpaceRequestError
from utils.responses import ApiException, ApiResult

"""
create_app.py
====================================
Holds the configuration functions for blueprints, routes, cors, error catching and much more.
"""


class ApiFlask(Flask):
    """
        Custom class extended from the Flask app object.
        Overrides the make response method to add custom error classes ApiResult and ApiException support
    """

    def __init__(self, import_name):
        super().__init__(import_name)

    def make_response(self, rv):
        """
            Return a response object which you can use to attach headers and registers the ApiResult and ApiException
            classes as response objects.
            Returns
            -------
                    Instance of a Flask Response class.
        """
        if isinstance(rv, ApiResult):
            return rv.to_response()
        if isinstance(rv, ApiException):
            return rv.to_response()
        return Flask.make_response(self, rv)

    def create_app(self, config=None):
        """
            Sets up this class instance by configuring database connections, endpoints, cors, secrets, origins, error
            handlers and JWT manager.
            Parameters
            ----------
                config
                    the file to be used as the configuration file
            Returns
            -------
                self
                    Instance of the ApiFlask class.
                    :param self:
        """

        with self.app_context():
            # Set all variables from the config file passed as a parameter
            self.config.from_object(config or {})

            # TODO: Setup CORS for all endpoints
            self.register_cors()

            # Setup blueprints to establish all endpoint routes
            self.register_blueprints()

            # Register the error handlers
            self.register_error_handlers()

            # Register database
            register_database(self)

            # register '/ endpoint'
            self.register_base_url()

            return self

    def register_blueprints(self):
        """Register all blueprints under the {.blueprint} module
        in the passed application instance.
        Arguments:
            app {flask application} -- application instance
        """
        for name in find_modules('blueprints'):
            mod = import_string(name)
            if hasattr(mod, 'bp'):
                self.register_blueprint(mod.bp)

    def register_error_handlers(self):
        """Register error daos to flask application instance.
        Arguments:
            app {flask application} -- application instance
        """
        if self.config['DEBUG'] == 0:

            # Register marshmallow validator  exceptions
            for name, obj in inspect.getmembers(sys.modules['marshmallow.exceptions']):
                if inspect.isclass(obj):
                    @self.errorhandler(obj)
                    def handle_marshmallow_errors(error):
                        return ApiException(
                            error_type='Validation Error',
                            message='Please verify you request body and parameters.',
                            status=400
                        )
            # Register mongoengine  exceptions
            for name, obj in inspect.getmembers(sys.modules['mongoengine.errors']):
                if inspect.isclass(obj) and not name == 'defaultdict':
                    @self.errorhandler(obj)
                    def handle_database_errors(error):
                        return ApiException(
                            error_type='Database Connection Error',
                            message='Internal Server Error',
                            status=500
                        )

            @self.errorhandler(SearchSpaceApiError)
            def handle_api_error(error):
                return ApiException(
                    error_type=error.error_type,
                    message=error.msg,
                    status=error.status
                )

            @self.errorhandler(SearchSpaceRequestError)
            def handle_request_error(error):
                return ApiException(
                    error_type=error.error_type,
                    message=error.msg,
                    status=error.status
                )

            @self.errorhandler(Exception)
            def handle_unexpected_error():
                return ApiException(
                    error_type='Unexpected Error',
                    message='An unexpected error has occurred.',
                    status=500
                )

        self.register_error_handler(
            400,
            lambda err: ApiException(message=str(
                err), status=400, error_type='Bad request')
        )

        self.register_error_handler(
            404,
            lambda err: ApiException(message=str(
                err), status=404, error_type='Not found')
        )

        self.register_error_handler(
            405,
            lambda err: ApiException(message=str(
                err), status=405, error_type='Request method')
        )

    def register_base_url(self):
        @self.route('/')
        def api():
            return ApiResult(
                message='You have reached the SearchSpace API. To make other requests please use all routes '
                        'under /searchSpace/api')

    def register_cors(self):
        """
            Setup CORS, cross-origin-resource-sharing settings
            Parameters
            ----------
                app
                    the ApiFlask application instance.
        """

        origins_list = '*'

        methods_list = ['GET', 'POST', 'OPTIONS']

        allowed_headers_list = [
            'Access-Control-Allow-Credentials',
            'Access-Control-Allow-Headers',
            'Access-Control-Allow-Methods',
            'Access-Control-Allow-Origin',
            'Content-Type',
            'Authorization',
            'Content-Disposition',
            'Referrer-Policy',
            'Strict-Transport-Security',
            'X-Frame-Options',
            'X-Xss-Protection',
            'X-Content-Type-Options',
            'X-Permitted-Cross-Domain-Policies'
        ]

        CORS(
            app=self,
            resources={r"/*": {"origins": origins_list}},
            methods=methods_list,
            allowed_headers=allowed_headers_list,
            supports_credentials=True,

        )
