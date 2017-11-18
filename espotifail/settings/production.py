import os 

from .base import *

import dj_database_url

DEBUG = False

SECRET_KEY = os.getenv("SECRET_KEY", None)

ALLOWED_HOSTS = ["https://espotifail.herokuapp.com/"]

DATABASES = dict()

# lee la variable de entorno de heroku, timeout 500s
DATABASES["default"] = dj_database_url.config(conn_max_age=500)

STATIC_ROOT = os.path.join(os.getcwd(), "static")
