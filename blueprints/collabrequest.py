import marshmallow
from flask import Blueprint, request, current_app
from json import load

from google.auth.transport import requests
from google.oauth2 import id_token
from mongoengine.errors import ValidationError, DoesNotExist
from utils.exceptions import SearchSpaceRequestError, SearchSpaceRequestValidationError
from utils.responses import ApiResult
from utils.validators import GetCollaboratorRequestValidator
from DAOs.dao_SS import *

bp = Blueprint('collab_request', __name__, url_prefix='/collab-request/')

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
    except ():
        raise SearchSpaceRequestValidationError(msg='Invalid Data', status=400)
    first_name = body.get('firstName')
    last_name = body.get('lastName')
    email = body.get('email')
    token = body.get('idToken')
    id_info = id_token.verify_oauth2_token(
        token,
        requests.Request(),
        current_app.config['GOOGLE_OAUTH_CLIENT_ID'])

    # Verify that the token was indeed issued by google accounts.
    if id_info['iss'] != 'accounts.google.com':
        raise SearchSpaceRequestValidationError(msg="Wrong issuer. Token issuer is not Google.")
    try:
        post_access_request(first_name=first_name, last_name=last_name, email=email)
        return ApiResult(
            status=201,
            message='Valid Data')
    except ():
        raise SearchSpaceRequestError(msg='Request already created', status=409)


