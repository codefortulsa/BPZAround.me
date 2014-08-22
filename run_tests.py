#!/usr/bin/env python
from __future__ import print_function

from os import environ
import sys

from django.conf import settings


def base_config():
    '''Create a minimal Django configuration'''
    return {
        'INSTALLED_APPS': ['south', 'django_nose', 'bpz'],
        'TEST_RUNNER': 'django_nose.NoseTestSuiteRunner',
        'DATABASE_ENGINE': 'django.contrib.gis.db.backends.postgis',
        'DATABASES': {
            'default': {
                'ENGINE': 'django.contrib.gis.db.backends.postgis',
                'NAME': 'bpzaroundme',
                'USER': 'bpzaroundme',
            }
        },
        'DEBUG': True,
        'TEMPLATE_DEBUG': True
    }


def test_config():
    '''Create a Django configuration for running tests'''

    config = base_config()

    if environ.get('POSTGIS_VERSION'):
        raw_postgis_version = environ['POSTGIS_VERSION']
        config['POSTGIS_VERSION'] = tuple(
            int(x) for x in raw_postgis_version.split('.'))

    # Optionally update configuration
    try:
        import test_overrides
    except ImportError:
        pass
    else:
        config = test_overrides.update(config)

    return config


def main(*paths):
    config = test_config()
    settings.configure(**config)

    from django.core import management
    failures = management.call_command('test', *paths)
    sys.exit(failures)


if __name__ == '__main__':
    # Extract non-options from command line
    # Options (-sx, --ipdb) will be parsed inside call_command
    paths = []
    for arg in sys.argv[1:]:
        if not arg.startswith('-'):
            paths.append(arg)

    main(*paths)
