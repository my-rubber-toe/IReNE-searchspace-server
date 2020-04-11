from flask import Blueprint

from utils.responses import ApiResult
from DAOs.dao_SS import *

bp = Blueprint('filters', __name__, url_prefix='/api/filters/')

#  TODO verify sessions  #
@bp.route('/', methods=['GET'])
def request_filters():
    """

    :return:
    """
    #  add exception  #
    #  DAO here  #
    damages = json.load(get_damage_list())
    damages
    return ApiResult(
        message=damages
    )

@bp.route('/tags')
def get_tags():
    #  add exception  #
    #  DAO here  #
    return ApiResult(
        message=get_tags_list()
    )


@bp.route('/infrastructure')
def get_infrastructures():
    #  add exception  #
    #  DAO here  #
    return ApiResult(
        message=get_infrastructure_list()
    )


@bp.route('/damage')
def get_damages():
    #  add exception  #
    #  DAO here  #
    return ApiResult(
        message=get_damage_list()
    )


@bp.route('/creators')
def get_creators():
    #  add exception  #
    #  DAO here  #
    return ApiResult(
        message=get_collaborators()
    )
