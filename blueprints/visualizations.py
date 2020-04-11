from flask import Blueprint, request
from DAOs.dao_SS import *
from utils.exceptions import SearchSpaceApiError
from utils.responses import ApiResult
from utils.validators import GetDocumentsValidator, GetComparisonValidator, GetDocIdValidator

bp = Blueprint('visualizations', __name__, url_prefix='/api/visualize/')

#TODO verify sessions
@bp.route('/map', methods=['GET'])
def visualize_map():
    """

    :return:
    """
    #  search in the DB for the document  #
    #  add exceptions for other methods  #
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


@bp.route('/comparison-graph', methods=['GET'])
def visualize_comparison():
    """

    :return:
    """
    # add exceptions for other methods
    if request.method == 'POST':
        if request.json == {}:
            raise SearchSpaceApiError(msg='No request body data.', status=400)
        body = GetComparisonValidator().load(request.json)
        #  DAO here  #
        return ApiResult(
            message='id of document', given_data=body
        )


@bp.route('/timeline/', methods=['GET'])
def visualize_timeline():
    """
    :return:
    """
    # add dao
    timeline = get_timeline_docs()
    return ApiResult(
        message='Data for visualize', given_data=timeline
    )
