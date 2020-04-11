import json

from DAOs.schema_DB import *


def post_access_request(**ac_req):
    new_collab = Collaborator(first_name=ac_req["first_name"], last_name=ac_req["last_name"],
                              email=ac_req["email"])
    new_collab.save()


def get_docs():
    get_doc = DocumentCase.objects.filter(published=True)
    return json.loads(get_doc.to_json())


def get_doc(docid):
    get_doc = DocumentCase.objects.get(id = docid, published = True)
    return json.loads(get_doc.to_json())


def get_doc_damage_type(damage):
    get_docs = DocumentCase.objects.filter(damageDocList__contains = damage)
    return json.loads(get_docs.to_json())


def get_doc_infrastructure_type(infras):
    get_docs = DocumentCase.objects.filter(infrasDocList__contains = infras)
    return json.loads(get_docs.to_json())


def get_doc_tag_type(tag):
    get_docs = DocumentCase.objects.filter(tagsDoc__contains = tag)
    return json.loads(get_docs.to_json()) 


#test it
def get_doc_creators():
    get_docs = DocumentCase.objects()
    get_creators_ids = []
    for doc in get_docs:
        get_creators_ids.append(doc.creatoriD)
    creators_names = []
    for idCollab in get_creators_ids:
        get_creator = Collaborator.objects.get(id=idCollab)
        creators_names.append(get_creator.first_name + " " + get_creator.last_name)
    return creators_names


def get_collaborators():
    collaborators = Collaborator.objects.only('first_name', 'last_name').exclude('id')
    return json.loads(collaborators.to_json())


#test it
def alphabetical_order():
    orderd_docs = DocumentCase.objects().order_by('title')
    return json.loads(orderd_docs.to_json())


def get_infrastructure_list():
    infra_objects = Infrastructure.objects().exclude("id")
    return json.loads(infra_objects.to_json())


def get_damage_list():
    damage_objects = Damage.objects().exclude("id")
    return json.loads(damage_objects.to_json())


def get_tags_list():
    tag_objects = Tag.objects().exclude("id")
    return json.loads(tag_objects.to_json())
