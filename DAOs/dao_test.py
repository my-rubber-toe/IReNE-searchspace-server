from mongoengine import *
from DAOs.schema_DB import *
from dao_SS import *
import json
import init_db_test
"""
    DAO_SS_1 (DAO created new collab)
"""
# new_fn = 'Aurora'
# new_ln = 'Black'
# new_email= 'aurora.black@upr.edu'
# post_access_request(first_name=new_fn,last_name=new_ln,email=new_email)
# new_collab = Collaborator.objects.get(email=new_email)
# print("name: ", new_collab.first_name,new_collab.last_name, "email: ",new_collab.email)

"""
    DAO_SS_2 (DAOs which returns a list of all documents published with different info for each 
    visualization in the UI )
"""
# print('docs for Timeline View:')
# print(get_timeline_docs())
# print('docs for Comparison View:')
# print(get_comparison_docs())
# print('docs for Map View:')
# print(get_map_docs())

"""
    DAO_SS_3 (DAOs which returns documents by filtering by the category given)
"""
# print("By Damage:")
# print(get_doc_damage_type('Flooding'))
# print("By Infrastructure:")
# print(get_doc_infrastructure_type('Energy'))
# print("By Tag:")
# print(get_doc_tag_type('Rain'))