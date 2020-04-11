from flask import Blueprint, request
from json import *
from utils.exceptions import SearchSpaceApiError
from utils.responses import ApiResult
from utils.validators import GetCollaboratorRequestValidator
from DAOs.dao_SS import *

bp = Blueprint('collab_request', __name__, url_prefix='/api/collab-request/')

#  TODO verify sessions  #
@bp.route('/', methods=['POST'])
def request_access():
    """

    :return:
    """
    #  add exception  #
    if request.json == {}:
        raise SearchSpaceApiError(msg='No request body data.', status=400)
    body = GetCollaboratorRequestValidator().load(request.json)
    first_name = body.get('first_name')
    last_name = body.get('last_name')
    email = body.get('email')
    db_response = post_access_request(first_name=first_name, last_name=last_name, email=email)

       #  DAO here  #
    return ApiResult(
        status=201,
        message='Valid Data', given_data=db_response
    )

