from flask import Blueprint, request

from DAOs.dao_SS import *
from utils.exceptions import SearchSpaceApiError
from utils.responses import ApiResult
from utils.validators import GetDocumentsValidator
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

        return ApiResult(
            message=get_docs()
        )
    if request.json == {}:
        raise SearchSpaceApiError(msg='No request body data.', status=400)
    body = GetDocumentsValidator().load(request.json)
    #  DAO here  #
    return ApiResult(
        message='Valid Data', given_data=body
    )


@bp.route('/view/<doc_id>', methods=['GET'])
def get_document(doc_id):
    """

    :return:
    """
    # identification = GetDocIdValidator().load(doc_id)
    #  search in the DB for the document  #

    return ApiResult(
        message=get_doc(doc_id)
    )

