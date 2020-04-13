from mongoengine import *
from schema_DB import *
import json

"""
    DAO_SS_1 (DAO created new collab)
"""
new_fn = 'Aurora'
new_ln = 'Black'
new_email= 'aurora.black@upr.edu'
post_access_request(first_name=new_fn,last_name=new_ln,email=new_email)
new_collab = Collaborator.objects.get(email=new_email)
print("name: ", new_collab.first_name,new_collab.last_name, "email: ",new_collab.email)