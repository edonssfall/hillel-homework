from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dz7_db',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'db',
        'PORT': '5432',

    }
}
