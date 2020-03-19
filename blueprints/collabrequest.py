from flask import Blueprint, g, current_app, request, session, make_response, jsonify

from utils.exceptions import SearchSpaceApiError
from utils.responses import ApiException, ApiResult
from utils.validators import GetCollaboratorRequestValidator

import datetime

bp = Blueprint('collab_request', __name__, url_prefix='/api/collab-request/')

#TODO verify sessions
@bp.route('/', methods=['POST'])
def request_access():
    """

    :return:
    """
    #add exception
    if request.json == {}:
        raise SearchSpaceApiError(msg='No request body data.', status=400)
    body = GetCollaboratorRequestValidator().load(request.json)
    #  DAO here  #
    return ApiResult(
        message='Valid Data', given_data=body
    )

