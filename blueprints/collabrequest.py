"""
collabrequest.py
====================================
Routes that manage the creation of collaborators request
"""
from flask import Blueprint, request, current_app
from google.auth.transport import requests
from google.oauth2 import id_token

from DAOs.dao_SS import *
from utils.exceptions import SearchSpaceRequestError, SearchSpaceRequestValidationError
from utils.responses import ApiResult
from utils.validators import GetCollaboratorRequestValidator

bp = Blueprint('collab_request', __name__, url_prefix='/collab-request/')


#  TODO verify sessions  #
@bp.route('/', methods=['POST'])
def request_access():
    """
    This route is for the creation of a Collaborator Request in the database. In the body of the POST request is
    required to send the first_name, last_name, email and google token for the creation of the request.

    Returns
    -------
    A message with status code 201 if the request was created
    A 500  error if the Database found a duplicate or
    A 400 error if invalid data is found.

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

    # Verify that the token was indeed issued by google accounts and that the token was issued for the collaborator
    # email.
    if id_info['iss'] != 'accounts.google.com':
        raise SearchSpaceRequestValidationError(msg="Wrong issuer. Token issuer is not Google.", status=400)
    if id_info['email'] != email:
        raise SearchSpaceRequestValidationError(msg="Token was not issued for this email", status=400)
    try:
        post_access_request(first_name=first_name, last_name=last_name, email=email)
        return ApiResult(
            status=201,
            message='Valid Data')
    except ():
        raise SearchSpaceRequestError(msg='Request already created', status=409)
