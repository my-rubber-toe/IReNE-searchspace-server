from flask import Blueprint, g, current_app, request, session, make_response, jsonify
from utils.responses import ApiException, ApiResult
from uuid import uuid4

import datetime

bp = Blueprint('documents', __name__, url_prefix='/api/documents/')

#TODO verify sessions
@bp.route('/', methods=['GET'])
def list_documents():
    """

    :return:
    """
    temp_response = {
        "response": 'List of documents metadata fitting the criteria in the request body.'
    }
    return ApiResult(
        value=temp_response
    )


@bp.route('/view/<doc_id>', methods=['GET'])
def get_document(doc_id):
    """

    :return:
    """
    #search in the DB for the document

    temp_response = {
        "document": 'document json doc_id',
        "doc_id": doc_id
    }
    return ApiResult(
        value=temp_response
    )

