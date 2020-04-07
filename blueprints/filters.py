from flask import Blueprint, request
from utils.exceptions import SearchSpaceApiError
from utils.responses import ApiException, ApiResult
from utils.validators import GetCollaboratorRequestValidator

bp = Blueprint('filters', __name__, url_prefix='/api/filters/')

#  TODO verify sessions  #
@bp.route('/', methods=['GET'])
def request_filters():
    """

    :return:
    """
    return ApiResult(
        message='Filters information'
    )
    #  add exception  #
    #  DAO here  #

