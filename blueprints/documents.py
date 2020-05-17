"""
documents.py \n
Routes that manage retrieval of documents for /documents route on Front End
"""
from flask import Blueprint, request

from DAOs.dao_SS import *
from utils.exceptions import SearchSpaceRequestError, SearchSpaceApiError
from utils.responses import ApiResult

bp = Blueprint('documents', __name__, url_prefix='/documents/')


@bp.route('/', methods=['GET'])
def list_documents():
    """
    GET request to return the metadata of all documents for /documents route on FE sending only the parts of the
    documents that are needed. This reduced the size to transfer.

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
            creatorInfo = get_doc_creator(doc['creatoriD']['$oid'])
            doc['creatorFullName'] = (creatorInfo['first_name'] + " " + creatorInfo['last_name'])
        return ApiResult(
            message=docs
        )
    raise SearchSpaceApiError(msg="Invalid Method", status=405)


@bp.route('/view/<string:doc_id>', methods=['GET'])
def get_document(doc_id):
    """

    GET request to return all the information about a specific document. This route is to retrieve the entire document.

    Parameters
    ----------
    doc_id
        id of the requested document

    Returns
    -------
    Message: json
        All Information of the requested document and status code 200.

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
        print(doc)
        creatorInfo = get_doc_creator(doc['creatoriD']['$oid'])
        doc['creatorFullName'] = (creatorInfo['first_name'] + " " + creatorInfo['last_name'])
        doc['creatorEmail'] = (creatorInfo['email'])
        return ApiResult(
            message=doc
        )
    except():
        raise SearchSpaceRequestError(msg="Invalid Request", status=400)
