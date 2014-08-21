from .base import *  # flake8: noqa

# Parse database configuration for $DATABASE_URL
import dj_database_url
# settings for Heroku Postgres DB
DATABASES['default'] = dj_database_url.config(default='postgres://localhost')

DEBUG = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ('gunicorn',)

SECRET_KEY = os.environ['SECRET_KEY']
