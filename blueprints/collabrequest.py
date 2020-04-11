import marshmallow
from flask import Blueprint, request
from json import *
from mongoengine import errors
from utils.exceptions import SearchSpaceApiError, SearchSpaceError, SearchSpaceRequestError, \
    SearchSpaceRequestValidationError
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
    try:
        body = GetCollaboratorRequestValidator().load(request.json)
    except marshmallow.ValidationError as e:
        raise SearchSpaceRequestValidationError(e)
    first_name = body.get('first_name')
    last_name = body.get('last_name')
    email = body.get('email')
    try:
        post_access_request(first_name=first_name, last_name=last_name, email=email)
        return ApiResult(
            status=201,
            message='Valid Data')
    except errors.NotUniqueError as e:
        raise SearchSpaceRequestError(e)


