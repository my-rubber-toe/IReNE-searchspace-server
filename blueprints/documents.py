from flask import Blueprint, request
from utils.exceptions import SearchSpaceRequestError
from utils.responses import ApiResult
from mongoengine.errors import DoesNotExist, ValidationError
from DAOs.dao_SS import *

bp = Blueprint('documents', __name__, url_prefix='/api/documents/')

#TODO verify sessions
@bp.route('/', methods=['GET'])
def list_documents():
    """
    GET request to return the metadata of all documents.

    Returns
    -------
    Message: json
       the metadata of all documents and status code 200.

    """
    if request.method == 'GET':
        docs = get_docs()
        return ApiResult(
            message=docs
        )


@bp.route('/view/<string:doc_id>', methods=['GET'])
def get_document(doc_id):
    """

    GET request to return all the information about a specific document.

    Parameters
    ----------
    doc_id
        id of the requested document

    Returns
    -------
    Message: json
        Information of the requested document and status code 200.

    Raises
    ------
    Validation Error
        If one of the fields is not valid with the specified schema of the Database
    DoesNotExists
        If the requested documents not exists on the Database

    """
    #  search in the DB for the document  #
    try:
        return ApiResult(
            message=get_doc(doc_id)
        )
    except (DoesNotExist, ValidationError) as e:
        raise SearchSpaceRequestError(err=e, msg="Invalid Id", status=409)

