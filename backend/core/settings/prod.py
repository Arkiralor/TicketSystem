from core.settings.settings import *

ENV_TYPE = 'prod'
DEBUG = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'log_file': {
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'formatter': 'verbose',
            'encoding': 'utf-8',
        },
    },
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s|%(asctime)s.%(msecs)d|%(name)s|%(module)s|%(funcName)s:%(lineno)s]    %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
    },
    'loggers': {
        'root': {
            'handlers': ['log_file',],
            "level": 'INFO'
        },
    },
}