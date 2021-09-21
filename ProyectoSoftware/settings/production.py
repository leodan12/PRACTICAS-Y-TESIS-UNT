# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['practicastesisunt.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'dflbjvkq4ug87q',
        'USER':'bxlfibqwqpfddw',
        'PASSWORD':'3a325632e289c2da19233244e9dc87937bade9aab900f93801ce8e7c0f79e7d1',
        'HOST':'ec2-44-194-6-121.compute-1.amazonaws.com',
        'DATABASE_PORT':'5432',
        
    }
}

STATICFILES_DIRS = (BASE_DIR,'static')

