from .base import *
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = ['latestnewstrends.herokuapp.com']

DATABASES = {}

DATABASES['default'] = dj_database_url.config(conn_max_age=600)