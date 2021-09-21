# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'dbProyectoSoftware1',
        'USER':'postgres',
        'PASSWORD':'123456789',
        'HOST':'127.0.0.1',
        'DATABASE_PORT':'5432',
        
    }
}
