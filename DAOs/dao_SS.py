from mongoengine import *
from schema_DB import *
import json

def get_doc_collab(collabid):
    get_docs = Document.objects.filter(creatoriD= collabid)
    return json.loads(get_docs.to_json())

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