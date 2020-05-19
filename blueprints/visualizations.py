"""
visualizations.py \n
Routes that manage retrieval of documents metadata for this features on Front End
"""
from flask import Blueprint
from DAOs.dao_SS import *
from utils.responses import ApiResult

bp = Blueprint('visualizations', __name__, url_prefix='/visualize/')


@bp.route('/map/', methods=['GET'])
def visualize_map():
    """
    GET request to return the metadata of all documents but only the fields fields needed for the map.

    Returns
    -------
    Message: json
       The metadata of all documents with only the required information for the map

    """
    map_docs = get_map_docs()
    return ApiResult(
        message=map_docs
    )


@bp.route('/comparison-graph/', methods=['GET'])
def visualize_comparison():
    """
    GET request to return the metadata of all documents but only the fields fields needed for the xy plot.

    Returns
    -------
    Message: json
       The metadata of all documents with only the required information for the xy plot

    """
    comparison = get_comparison_docs()
    return ApiResult(
        message=comparison
    )


@bp.route('/timeline/', methods=['GET'])
def visualize_timeline():
    """
    GET request to return the metadata of all documents but only the fields fields needed for the timeline.

    Returns
    -------
    Message: json
       The metadata of all documents with only the required information for the timeline

    """
    timeline = get_timeline_docs()
    return ApiResult(
        message=timeline
    )
