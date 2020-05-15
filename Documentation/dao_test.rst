dao\_test module
================

- DAO_SS_1 (DAO creates new collab from Access Request)
   - post_access_request(first_name=new_fn,last_name=new_ln,email=new_email)
- DAO_SS_2 (DAOs which returns a list of all documents published with different info for each visualization in the UI )
   - get_timeline_docs()
   - get_comparison_docs()
   - get_map_docs()
- DAO_SS_3 (DAOs which returns documents by filtering by the category given)
   - get_doc_damage_type(damageType)
   - get_doc_infrastructure_type(infrastructureType)
   - get_doc_tag_type(tagItem)

.. automodule:: dao_test
   :members:
