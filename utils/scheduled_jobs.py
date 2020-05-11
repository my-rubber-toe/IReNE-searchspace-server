"""
scheduled_jobs.py
====================================
Scheduling operations.
"""

from flask import current_app

from utils.logger import AppLogger
from mongoengine import connection
import time
import threading


def ping_db():
    """
        Send ping command to the system database to check health.
        If the ping fails , register the error in app.log
    """
    while True:
        if not connection.get_db().command('ping'):
            logger: AppLogger = current_app.__getattribute__('app_logger')
            logger.log_error('Database Connection Error')
        time.sleep(10)


class ScheduledJobs:
    """
        Static Class intended to hold all Scheduled operations. Operations run as a background thread.
    """

    @staticmethod
    def job_ping_db():
        """
            Static method that runs the function "ping_db" as a scheduled job.
        """
        t = threading.Thread(name='ping_db', target=ping_db)
        t.daemon = True
        t.start()
