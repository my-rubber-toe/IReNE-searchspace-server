"""
init_db.py
====================================
This file contains all essential operations to start and register this app's database connection as part of the
current application context.
"""

from mongoengine import *
from config import environment


def register_database(app):
    """
        Register the server's database connection as part of the current app context.
        Parameters
        ----------
            app
                an ApiFlask class instance
    """
    app.__setattr__('db', connect(db=environment.DB_NAME, host=environment.DB_HOST))
