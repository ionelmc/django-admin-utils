from pathlib import Path

BASE_DIR = Path(__file__).parent
DEBUG = True
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = str(BASE_DIR / 'database.sqlite')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        # 'NAME': 'test.sqlite',
    },
}
APPEND_SLASH = True
USE_TZ = True
ALLOWED_HOSTS = ('*',)
INSTALLED_APPS = (
    'pghistory',
    'pghistory.admin',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'test_app.apps.TestAppConfig',
)
MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
)
SITE_ID = 1
ROOT_URLCONF = 'test_project.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR / 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    }
]
SECRET_KEY = "DON'T MATTER"  # noqa: S105
STATIC_URL = '/static/'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s: %(levelname)s/%(processName)s/%(process)s] %(name)s - %(message)s '
            '\t\t\t in %(funcName)s@%(pathname)s:%(lineno)d'
        },
    },
    'handlers': {
        'console': {'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': 'verbose', 'stream': 'ext://sys.stderr'},
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True,
    },
}
