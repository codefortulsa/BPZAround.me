#!/usr/bin/env python
from __future__ import print_function

import sys
from os import environ

from django.conf import settings
import dj_database_url


def base_config():
    '''Create a minimal Django configuration'''
    config = {
        'INSTALLED_APPS': ['south', 'django_nose', 'bpz'],
        'TEST_RUNNER': 'django_nose.NoseTestSuiteRunner',
        'DATABASES': {
            'default': dj_database_url.config(
                default='postgis://bpzaroundme@/bpzaroundme'),
        },
        'DEBUG': True,
        'TEMPLATE_DEBUG': True
    }

    if environ.get('POSTGIS_VERSION'):
        raw_postgis_version = environ['POSTGIS_VERSION']
        config['POSTGIS_VERSION'] = tuple(
            int(x) for x in raw_postgis_version.split('.'))

    return config


def test_config():
    '''Create a Django configuration for running tests'''
    config = base_config()
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
