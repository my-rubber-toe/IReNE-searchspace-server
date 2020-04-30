from flask import Flask
from flask_cors import CORS
from werkzeug.utils import find_modules, import_string
from utils.responses import ApiException, ApiResult
# from DAOs import init_db_test

class ApiFlask(Flask):
    """
        Custom class extended from the Flask app object.
        Overrides the make response method to add custom error classes ApiResult and ApiException support
    """

    def make_response(self, rv):
        if isinstance(rv, ApiResult):
            return rv.to_response()
        if isinstance(rv, ApiException):
            return rv.to_result()
        return Flask.make_response(self, rv)


# Setup Methods

def create_app(config=None):
    """Creates and returns a Flask app instance.
    Keyword Arguments:
        config {string} --  (default: {None})
    Returns:
        [flask_application] -- instance of a flask app
    """
    app = ApiFlask(__name__)

    with app.app_context():
        # Set all variables from the config file passed as a parameter
        app.config.from_object(config or {})

        # Setup Flask session Secret
        # app.secret_key = app.config['SECRET_KEY']

        # TODO: Setup CORS for all endpoints
        register_cors(app)

        # Testing with mock DB
        # Setup validator plugins
        # validator.init_app(app)

        # Setup blueprints to establish all endpoint routes
        register_blueprints(app)

        # Register the error handlers
        register_error_handlers(app)

        # register '/SearchSpace/api endpoint'
        register_base_url(app)

        # Setup app request teardown process
        register_request_teardown(app)

        return app


def register_blueprints(app):
    """Register all blueprints under the {.blueprint} module
    in the passed application instance.
    Arguments:
        app {flask application} -- application instance
    """
    for name in find_modules('blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)


def register_error_handlers(app):
    """Register error daos to flask application instance.
    Arguments:
        app {flask application} -- application instance
    """
    # if app.config['DEBUG']:
    #     # If debug true, then return the whole error stack
    #     @app.errorhandler(SearchSpaceError)
    #     def handle_error(error):
    #         return ApiException(
    #             _type=error.__class__.__name__,
    #             message=error.error_stack,
    #             status=error.status
    #         )
    # else:
    #     @app.errorhandler(SearchSpaceError)
    #     def handle_general_error(error):
    #         return ApiException(
    #             _type=error.__class__.__name__,
    #             message=error.msg,
    #             status=error.status
    #         )
    #
    #     @app.errorhandler(SearchSpaceApiError)
    #     def handle_api_error(error):
    #         # send email to service desk
    #         return ApiException(
    #             _type=error.__class__.__name__,
    #             message=error.msg,
    #             status=error.status
    #         )
    #
    #     @app.errorhandler(Exception)
    #     def handle_unexpected_error(error):
    #         SearchSpaceError(
    #             err=error,
    #             msg='An unexpected error has occurred.',
    #             status=500
    #         ).log()
    #         return ApiException(
    #             _type='UnexpectedException',
    #             message='An unexpected error has occurred. Please verify error logs',
    #             status=500
    #         )
    #
    # app.register_error_handler(
    #     400,
    #     lambda err: ApiException(message=str(
    #         err), status=400, _type='Bad request')
    # )
    #
    # app.register_error_handler(
    #     404,
    #     lambda err: ApiException(message=str(
    #         err), status=404, _type='Not found')
    # )
    #
    # app.register_error_handler(
    #     405,
    #     lambda err: ApiException(message=str(
    #         err), status=405, _type='Request method')
    # )


def register_base_url(app):
    @app.route('/')
    def api():
        return ApiResult(message='You have reached the SearchSpace API. To make other requests please use all routes under /searchSpace/api')



def register_request_teardown(app):
    @app.teardown_request
    def do_the_thing(exeption):
        pass

    pass


def register_cors(app: Flask):
    """
        Setup CORS , cross-origin-resource-sharing settings
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
        app=app,
        resources={r"/*": {"origins": origins_list}},
        methods=methods_list,
        allowed_headers=allowed_headers_list,
        supports_credentials=True,

    )
