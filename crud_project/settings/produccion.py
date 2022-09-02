from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost','*']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'prueba',
        'USER': 'admin',
        'PASSWORD': 'pru3b44dm1n',
        'HOST': 'prueba.cpe6pww62uyr.us-east-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}