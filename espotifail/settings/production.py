import os 

from .base import *

import dj_database_url


SECRET_KEY = os.getenv("SECRET_KEY", None)

DEBUG = False

ALLOWED_HOSTS = [os.getenv("HOSTS", None)]

# lee la variable de entorno de heroku, timeout 500s
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DBNAME", None),
        'USER': os.getenv("DBUSER", None),
        'PASSWORD': os.getenv("DBPASS", None),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(os.getcwd(), "static")
