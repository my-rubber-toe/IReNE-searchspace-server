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
    filters = {'damages': [], 'tags': [], 'infrastructures': [], 'authors': []}
    filters['damages'].extend(get_damage_list())
    filters['tags'].extend(get_tags_list())
    filters['infrastructures'].extend(get_infrastructure_list())
    filters['authors'].extend(get_collaborators())
    return ApiResult(
        message=filters
    )

@bp.route('/tags')
def get_tags():
    #  add exception  #
    #  DAO here  #
    return ApiResult(
        message=get_tags_list()
    )


@bp.route('/infrastructures')
def get_infrastructures():
    #  add exception  #
    #  DAO here  #
    return ApiResult(
        message=get_infrastructure_list()
    )


@bp.route('/damages')
def get_damages():
    #  add exception  #
    #  DAO here  #
    return ApiResult(
        message=get_damage_list()
    )


@bp.route('/authors')
def get_creators():
    #  add exception  #
    #  DAO here  #
    return ApiResult(
        message=get_collaborators()
    )
