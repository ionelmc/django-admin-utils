import os
TEMPLATE_DEBUG = DEBUG = True
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(os.path.dirname(__file__), 'database.sqlite')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_NAME
    },
}
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'test_app',
)
SITE_ID = 1
ROOT_URLCONF = 'test_project.urls'
TEMPLATE_DIRS = os.path.join(os.path.dirname(__file__), 'templates'),
SECRET_KEY = "DON'T MATTER"
STATIC_URL = "/static/"
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s: %(levelname)s/%(processName)s/%(process)s] %(name)s - %(message)s \t\t\t in %(funcName)s@%(pathname)s:%(lineno)d'
        },
    },
    'handlers': {
        'console': {
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'verbose',
            'stream': 'ext://sys.stderr'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True,
    }
}
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
