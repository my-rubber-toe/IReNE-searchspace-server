from flask import Blueprint, request

from DAOs.dao_SS import *
from utils.exceptions import SearchSpaceRequestError
from utils.responses import ApiResult
from utils.validators import GetDocumentsValidator
from mongoengine import errors
from DAOs.dao_SS import *

bp = Blueprint('documents', __name__, url_prefix='/api/documents/')

#TODO verify sessions
@bp.route('/', methods=['GET'])
def list_documents():
    """

    :return:
    """
    if request.method == 'GET':
        #  getalldocuments
        #  DAO  #
        docs = get_docs()
        return ApiResult(
            message=docs
        )


@bp.route('/view/<doc_id>', methods=['GET'])
def get_document(doc_id):
    """

    :return:
    """
    # identification = GetDocIdValidator().load(doc_id)
    #  search in the DB for the document  #
    try:
        return ApiResult(
            message=get_doc(doc_id)
        )
    except errors.DoesNotExist as e:
        raise SearchSpaceRequestError(e)

