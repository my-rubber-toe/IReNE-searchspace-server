from flask import Blueprint, request
from utils.responses import ApiException, ApiResult
from utils.validators import GetDocumentsValidator, GetDocIdValidator
from utils.exceptions import SearchSpaceApiError


bp = Blueprint('documents', __name__, url_prefix='/api/documents/')

#TODO verify sessions
@bp.route('/', methods=['GET', 'POST'])
def list_documents():
    """

    :return:
    """
    if request.method == 'GET':
        #  getalldocuments
        #  DAO  #
        return ApiResult(
            message='All Docs'
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
    identification = GetDocIdValidator().load(doc_id)
    #  search in the DB for the document  #

    return ApiResult(
        message='the id is '+identification
    )

