from flask import Blueprint, g, current_app, request, session, make_response, jsonify
from utils.responses import ApiResult, ApiException

route_prefix = f'{current_app.config["PREFIX_URL"]}/test'

bp = Blueprint('test', __name__, url_prefix=route_prefix)


@bp.route('/')
def test_main_route():
    return jsonify(message=f'You have arrived at {route_prefix}')


@bp.route('/api_result')
def test_api_result():
    return ApiResult(
        status=200,
        value={
            'message': 'I am the api_result route!'
        }
    )


@bp.route('/api_exception')
def test_api_exception():
    return ApiException(
        message='You are testing the ApiException class'
    )


@bp.before_request
def before_requests():
    print('Before requests in /api/test/')
