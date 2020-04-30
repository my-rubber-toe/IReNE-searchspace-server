from flask import Blueprint
from utils.responses import ApiResult
from DAOs.dao_SS import *

bp = Blueprint('filters', __name__, url_prefix='/filters/')

#  TODO verify sessions  #
@bp.route('/', methods=['GET'])
def request_filters():
    """
    GET request to return all the available filters options.

    Returns
    -------
    Message: json
       All the options of every category of the SearchSpace filters

    """
    #  DAOs to get the info  #
    filters = {'damages': [], 'tags': [], 'infrastructures': [], 'authors': []}
    filters['damages'].extend(get_damage_list())
    filters['tags'].extend(get_tags_list())
    filters['infrastructures'].extend(get_infrastructure_list())
    authors = get_authors()
    for author in authors:
            filters['authors'].append(author['author_FN'] + " " + author['author_LN'])
    return ApiResult(
        message=filters
    )

@bp.route('/tags')
def get_tags():
    """
    GET request to return all the available options of the filter category tags.

    Returns
    -------
    Message: json
       All the options to filter of the tags category

    """
    #  DAOs to get the info  #
    return ApiResult(
        message=get_tags_list()
    )


@bp.route('/infrastructures')
def get_infrastructures():
    """
    GET request to return all the available options of the filter category infrastructure.

    Returns
    -------
    Message: json
       All the options to filter of the infrastructure category

    """
    #  DAOs to get the info  #
    return ApiResult(
        message=get_infrastructure_list()
    )


@bp.route('/damages')
def get_damages():
    """
    GET request to return all the available options of the filter category damages.

    Returns
    -------
    Message: json
       All the options to filter of the damages category

    """
    #  DAOs to get the info  #
    return ApiResult(
        message=get_damage_list()
    )


@bp.route('/authors')
def get_creators():
    """
    GET request to return all the available options of the filter damage infrastructure.

    Returns
    -------
    Message: json
       All the options to filter of the damage category

    """
    #  DAOs to get the info  #
    authors = get_collaborators()
    for author in authors:
        author['fullName'] = author['first_name'] + " " + author['last_name']
    return ApiResult(
        message=authors
    )
