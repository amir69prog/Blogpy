from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}

CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = 'ckeditor/'