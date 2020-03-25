from mongoengine import *
from schema_DB import *
import json

def post_access_request(**ac_req):
    new_collab = Collaborator(first_name = ac_req["first_name"], last_name = ac_req["last_name"],
    email = ac_req["email"], faculty = ac_req["faculty"])
    new_collab.save()

def get_docs():
    get_doc = DocumentCase.objects()
    return json.loads(get_doc.to_json())

def get_doc(docid):
    get_doc = DocumentCase.objects.get(id = docid)
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