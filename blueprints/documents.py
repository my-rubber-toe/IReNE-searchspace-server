from flask import Blueprint, request
from utils.exceptions import SearchSpaceRequestError
from utils.responses import ApiResult
from mongoengine.errors import DoesNotExist, ValidationError
from DAOs.dao_SS import *

bp = Blueprint('documents', __name__, url_prefix='/documents')

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
        for doc in docs:
            doc['authorFullName'] = []
            for author in doc['author']:
                doc['authorFullName'].append(
                        author['author_FN'] + " " + author['author_LN'])
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
        doc = get_doc(doc_id)
        creatorInfo = get_doc_creator(doc['creatoriD'])
        doc['creatorFullName'] = (creatorInfo['first_name'] + " " + creatorInfo['last_name'])
        doc['creatorEmail'] = (creatorInfo['email'])
        return ApiResult(
            message=doc
        )
    except (DoesNotExist, ValidationError) as e:
        raise SearchSpaceRequestError(err=e, msg="Invalid Id", status=409)

