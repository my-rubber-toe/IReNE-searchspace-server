from flask import Blueprint, g, current_app, request, session, make_response, jsonify
from utils.responses import ApiException, ApiResult
from uuid import uuid4

import datetime

bp = Blueprint('visualizations', __name__, url_prefix='/api/visualize/')

#TODO verify sessions
@bp.route('/map', methods=['GET', 'POST'])
def visualize_map():
    """

    :return:
    """
    #search in the DB for the document
    # add exceptions for other methods
    title = ''
    description = ''
    authors = ''
    actors = ''
    publication_date1 = ''
    publication_date2 = ''
    incident_dates = ''
    infrastructure_type = ''
    damage_type = ''
    language = ''
    tags = {}
    if request.method == 'POST':
        title = request.form['title']
        temp_response = {
            "document": "doc_id",
            "title": title
        }
        #DAO here
        return ApiResult(
            value=temp_response
        )
    else:
        temp_response = {
            "document": "error"
        }
        return ApiResult(
            value=temp_response
        )


@bp.route('/comparison-graph', methods=['GET', 'POST'])
def visualize_comparison():
    """

    :return:
    """
    # add exceptions for other methods
    if request.method == 'POST':
        data = request.json
        xcat = data['xcategory']
        ycat = data['ycategory']
        xvalue = data['xvalue']
        yvalue = data['ycategory']
        #DAO here
        temp_response = {
            "category of x": xcat,
            "x value": xvalue,
            "category of y": ycat,
            "y value": yvalue,
            "message": "requested"
        }
        return ApiResult(
            value=temp_response
        )
    else:
        temp_response = {
            "document": "error"
        }
        return ApiResult(
            value=temp_response
        )


@bp.route('/timeline', methods=['GET', 'POST'])
def visualize_timeline():
    """
    :return:
    """
    # add exceptions for other methods
    if request.method == 'POST':
        data = request.json
        doc_id = data['doc_id']
        #DAO here
        temp_response = {
            "document": doc_id,
            "message": "requested timeline"
        }
        return ApiResult(
            value=temp_response
        )
    else:
        temp_response = {
            "document": "error"
        }
        return ApiResult(
            value=temp_response
        )
