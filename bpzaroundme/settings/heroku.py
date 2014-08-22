import os

from .base import *  # flake8: noqa

DEBUG = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ('gunicorn',)

SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)
STATIC_ROOT = 'staticfiles'
