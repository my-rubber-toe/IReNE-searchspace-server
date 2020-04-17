import marshmallow
from flask import Blueprint, request
from json import load
from mongoengine.errors import ValidationError, DoesNotExist
from utils.exceptions import SearchSpaceRequestError, SearchSpaceRequestValidationError
from utils.responses import ApiResult
from utils.validators import GetCollaboratorRequestValidator
from DAOs.dao_SS import *

bp = Blueprint('collab_request', __name__, url_prefix='/api/collab-request/')

#  TODO verify sessions  #
@bp.route('/', methods=['POST'])
def request_access():
    """
    This route is for the creation of a Collaborator Request in the database. In the body of the POST request is
    required to send the first_name, last_name and email for the creation of the request.

    Returns
    -------
    A message with status code 201 if the request was created
    A 500  status code with the message "Request already created" or "Invalid Data" if the information of the body is invalid.

    Raises
    ------
    Validation Error
        If one of the fields is not valid as specified with the validators of the server
    NotUniqueError
        If the request already is created in the database
    """
    try:
        body = GetCollaboratorRequestValidator().load(request.json)
    except (marshmallow.ValidationError, ValidationError) as e:
        raise SearchSpaceRequestValidationError(e, msg='Invalid Data')
    first_name = body.get('first_name')
    last_name = body.get('last_name')
    email = body.get('email')
    try:
        post_access_request(first_name=first_name, last_name=last_name, email=email)
        return ApiResult(
            status=201,
            message='Valid Data')
    except NotUniqueError as e:
        raise SearchSpaceRequestError(e, msg='Request already created')

