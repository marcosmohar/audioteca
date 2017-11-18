from .base import *
import os
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9l@5mvrha8_h3b=1lq2qnmld8!@!!-8f=g0vl6=ts8bj!n@&gs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'espotifail',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATICFILES_DIRS = [os.path.join(os.getcwd(), "static")]
