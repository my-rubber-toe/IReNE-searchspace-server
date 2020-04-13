from flask import Blueprint, request

from DAOs.dao_SS import *
from utils.exceptions import SearchSpaceRequestError
from utils.responses import ApiResult
from mongoengine.errors import DoesNotExist,ValidationError
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


@bp.route('/view/<string:doc_id>', methods=['GET'])
def get_document(doc_id):
    """

    :return:
    """
    #  search in the DB for the document  #
    try:
        return ApiResult(
            message=get_doc(doc_id)
        )
    except (DoesNotExist, ValidationError) as e:
        raise SearchSpaceRequestError(err=e, msg="Invalid Id", status=409)

