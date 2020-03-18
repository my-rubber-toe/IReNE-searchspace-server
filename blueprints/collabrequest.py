from flask import Blueprint, g, current_app, request, session, make_response, jsonify
from utils.responses import ApiException, ApiResult
from uuid import uuid4

import datetime

bp = Blueprint('collab_request', __name__, url_prefix='/api/collab-request/')

#TODO verify sessions
@bp.route('/', methods=['POST'])
def request_access():
    """

    :return:
    """
    #add exception
    data = request.json
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    #Insert DAO

    temp_response = {
        "response": 'Request processed',
        "First Name": first_name,
        "Last Name": last_name,
        "Email": email
    }
    return ApiResult(
        value=temp_response
    )
