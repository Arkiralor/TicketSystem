"""
Initialize the logger for the application.
"""
import logging

logger = logging.getLogger('ticket_system.' + __name__)
default_app_config = 'user_app.apps.UserAppConfig'