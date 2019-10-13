from .base import *
import dj_database_url

SECRET_KEY = '*gj75=l@zkh1!c5(@-17gfex5$aq1j_bwqgbbzm-n2faj)*m6v'

ALLOWED_HOSTS = ['.herokuapp.com']

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hayleyandnerd',
        'USER': 'hayley',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '',
    }
}
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)