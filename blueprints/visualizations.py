from flask import Blueprint
from DAOs.dao_SS import *
from utils.responses import ApiResult

bp = Blueprint('visualizations', __name__, url_prefix='/api/visualize/')

#TODO verify sessions
@bp.route('/map', methods=['GET'])
def visualize_map():
    """

    :return:
    """
    #  search in the DB for the document  #
    #  add exceptions for other methods  #
    #  DAO  #
    map_docs = get_map_docs()
    return ApiResult(
        message=map_docs
    )


@bp.route('/comparison-graph', methods=['GET'])
def visualize_comparison():
    """

    :return:
    """
    #  DAO here  #
    comparison = get_comparison_docs()
    return ApiResult(
        message=comparison
    )


@bp.route('/timeline', methods=['GET'])
def visualize_timeline():
    """
    :return:
    """
    # add dao
    timeline = get_timeline_docs()
    return ApiResult(
        message=timeline
    )
