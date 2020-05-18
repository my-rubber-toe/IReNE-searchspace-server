from bson.json_util import dumps

from DAOs.schema_DB import *


def post_access_request(**ac_req):
    """
        Creates new collab with approved = false
    """
    new_collab = collaborator(first_name=ac_req["first_name"], last_name=ac_req["last_name"],
                              email=ac_req["email"])
    new_collab.save()


def get_docs():
    """
        Returns the list of documens
    """
    docs = document_case.objects(published=True).aggregate(*[
        {
            '$lookup': {
                'from': collaborator._get_collection_name(),
                'localField': 'creatoriD',
                'foreignField': '_id',
                'as': 'creatorName'
            }
        },
        {
            '$project': {
                '_id': {'$toString': '$_id'},
                'title': 1,
                'language': 1,
                'incidentDate': 1,
                'creationDate': 1,
                'lastModificationDate': 1,
                'tagsDoc': 1,
                'infrasDocList': 1,
                'damageDocList': 1,
                'location': 1,
                'creatorFullName': {
                    '$let': {
                        'vars': {
                            'tmp': {'$arrayElemAt': ["$creatorName", 0]}
                        },
                        'in': {
                            '$concat': ['$$tmp.first_name', ' ', '$$tmp.last_name']
                        }
                    }
                },
                'authorFullName': {
                    '$map': {
                        'input': '$author',
                        'as': 'tmp',
                        'in': {
                            '$concat': ['$$tmp.author_FN', ' ', '$$tmp.author_LN']
                        }
                    }
                },

            }
        },
    ])
    return dumps(docs)


def get_doc(docid):
    """
        Returns a specific document
    """
    get_doc = document_case.objects(id=docid, published=True).aggregate(*[
        {
            '$lookup': {
                'from': collaborator._get_collection_name(),
                'localField': 'creatoriD',
                'foreignField': '_id',
                'as': 'creatorName'
            }
        },
        {
            '$project': {
                '_id': 0,
                'title': 1,
                'language': 1,
                'incidentDate': 1,
                'creationDate': 1,
                'lastModificationDate': 1,
                'tagsDoc': 1,
                'infrasDocList': 1,
                'damageDocList': 1,
                'location': 1,
                'author': 1,
                'actor': 1,
                'section': 1,
                'description': 1,
                'creatorFullName': {
                    '$let': {
                        'vars': {
                            'tmp': {'$arrayElemAt': ["$creatorName", 0]}
                        },
                        'in': {
                            '$concat': ['$$tmp.first_name', ' ', '$$tmp.last_name']
                        }
                    }
                },
                'creatorEmail': {
                    '$let': {
                        'vars': {
                            'tmp': {'$arrayElemAt': ["$creatorName", 0]}
                        },
                        'in': {
                            '$concat': ['$$tmp.email']
                        }
                    }
                },
                'authorFullName': {
                    '$map': {
                        'input': '$author',
                        'as': 'tmp',
                        'in': {
                            '$concat': ['$$tmp.author_FN', ' ', '$$tmp.author_LN']
                        }
                    }
                },

            }
        },
    ])
    return dumps(get_doc)


def get_doc_damage_type(damage):
    """
        Returns the list of documents based on category given
    """
    get_docs = document_case.objects.filter(damageDocList__contains=damage)
    return json.loads(get_docs.to_json())


def get_doc_infrastructure_type(infras):
    """
        Returns the list of documents based on category given
    """
    get_docs = document_case.objects.filter(infrasDocList__contains=infras)
    return json.loads(get_docs.to_json())


def get_doc_tag_type(tag):
    """
        Returns the list of documents based on category given
    """
    get_docs = document_case.objects.filter(tagsDoc__contains=tag)
    return json.loads(get_docs.to_json())


def get_doc_creator(collabId):
    get_creator = collaborator.objects().only('first_name', 'last_name', 'email').get(id=collabId)
    return json.loads(get_creator.to_json())


def get_collaborators():
    collaborators = collaborator.objects.only('first_name', 'last_name').exclude('id')
    return json.loads(collaborators.to_json())


def get_authors():
    authors = document_case.objects(published=True).only('author').distinct('author')
    return authors


def alphabetical_order():
    """
        Returns the list of documents in alphabetical order
    """
    orderd_docs = document_case.objects(published=True).order_by('title')
    return json.loads(orderd_docs.to_json())


def get_infrastructure_list():
    """
        Returns the list of infrastructures
    """
    infra_objects = infrastructure.objects().exclude("id")
    return json.loads(infra_objects.to_json())


def get_damage_list():
    """
        Returns the list of damages
    """
    damage_objects = damage.objects().exclude("id")
    return json.loads(damage_objects.to_json())


def get_tags_list():
    """
        Returns the list of tags
    """
    tag_objects = tag.objects()
    return json.loads(tag_objects.to_json())


def get_timeline_docs():
    """
        Returns the list documents with the metadata necessary for 
    """
    timeline_docs = document_case.objects(published=True).only('id', 'title', 'timeline',
                                                               'infrasDocList', 'damageDocList')

    return json.loads(timeline_docs.to_json())


def get_comparison_docs():
    comparison_docs = document_case.objects(published=True).only('id', 'title', 'tagsDoc',
                                                                 'infrasDocList', 'damageDocList', 'creationDate',
                                                                 'incidentDate')
    return json.loads(comparison_docs.to_json())


def get_map_docs():
    map_docs = document_case.objects(published=True).exclude('timeline', 'actor',
                                                             'creatoriD', 'description', 'section', 'published',
                                                             'author')
    return json.loads(map_docs.to_json())
