from .base import *

SECRET_KEY = '*gj75=l@zkh1!c5(@-17gfex5$aq1j_bwqgbbzm-n2faj)*m6v'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}