'''settings for BPZAround.me project

Designed for Heroku and http://12factor.net/config.  Configuration is
overriden by environment variables.

One way to set environment variables for local development in a virtualenv:

$ vi $VIRTUAL_ENV/bin/postactivate
export DJANGO_DEBUG=1
$ vi $VIRTUAL_ENV/bin/predeactivate
unset DJANGO_DEBUG
$ source $VIRTUAL_ENV/bin/postactivate

To set environment variables in heroku environment
$ heroku config
$ heroku config:set DJANGO_DEBUG=1

Environment variables:
ALLOWED_HOSTS - comma-separated list of allowed hosts
DATABASE_URL - See https://github.com/kennethreitz/dj-database-url
DJANGO_DEBUG - 1 to enable, 0 to disable, default disabled
EXTRA_INSTALLED_APPS - comma-separated list of apps to add to INSTALLED_APPS
POSTGIS_VERSION - "2.1.3" to set to version (2, 1, 3)
SECRET_KEY - Overrides SECRET_KEY
SECURE_PROXY_SSL_HEADER - "HTTP_X_FORWARDED_PROTOCOL,https" to enable
STATIC_ROOT - Overrides STATIC_ROOT
'''

from os import environ
from os.path import abspath, basename, dirname, join, normpath
from sys import path
import dj_database_url

DJANGO_ROOT = dirname(dirname(abspath(__file__)))
SITE_NAME = basename(DJANGO_ROOT)
path.append(DJANGO_ROOT)

DEBUG = environ.get("DJANGO_DEBUG", '0') in (1, '1')
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.config(
        default='postgis://bpzaroundme@/bpzaroundme'),
    # Equivalent to:
    # 'default': {
    #     'ENGINE': 'django.contrib.gid.db.backends.postgis',
    #     'NAME': 'bpzaroundme',
    #     'USER': 'bpzaroundme',
    # }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
if environ.get('STATIC_ROOT'):
    STATIC_ROOT = environ['STATIC_ROOT']
else:
    STATIC_ROOT = normpath(join(DJANGO_ROOT, 'staticfiles'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/
# STATICFILES_DIRS = (
#   normpath(join(DJANGO_ROOT, 'static')),
# )

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    # 'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = environ.get('SECRET_KEY', 'This_one_is_unsafe')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'jingo.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bpzaroundme.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'bpzaroundme.wsgi.application'
TEMPLATE_DIRS = (
    normpath(join(DJANGO_ROOT, 'templates')),
)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # Third-party apps
    'south',
    'django_nose',
    'rest_framework',

    # Our apps
    'bpz',
]
if environ.get('EXTRA_INSTALLED_APPS'):
    INSTALLED_APPS += environ['EXTRA_INSTALLED_APPS'].split(',')


SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': (
                "[%(asctime)s] %(levelname)s"
                " [%(name)s:%(lineno)s] %(message)s"),
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'standard',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Use django-nose to run tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# More overrides from environment

# https://docs.djangoproject.com/en/1.6/ref/contrib/gis/testing/#postgis-version
if environ.get('POSTGIS_VERSION'):
    raw_postgis_version = environ['POSTGIS_VERSION']
    POSTGIS_VERSION = tuple(int(x) for x in raw_postgis_version.split('.'))

# https://docs.djangoproject.com/en/1.6/ref/settings/#secure-proxy-ssl-header
if environ.get('SECURE_PROXY_SSL_HEADER'):
    raw = environ['SECURE_PROXY_SSL_HEADER']
    SECURE_PROXY_SSL_HEADER = tuple(raw.split(','))

# https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
if environ.get('ALLOWED_HOSTS'):
    ALLOWED_HOSTS = environ['ALLOWED_HOSTS'].split(',')
