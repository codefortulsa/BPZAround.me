#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import bpz

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    "Django >=1.6,<1.7",
    "South >= 1.0",
]

test_requirements = [
    "django-nose",
    "coverage",
]

setup(
    name='BPZAround.me',
    version=bpz.__version__,
    description=(
        'BPZAround.me alerts you when someone is building, planning,'
        ' or zoning around you.'),
    long_description=readme + '\n\n' + history,
    author='Code for Tulsa',
    author_email='captains@codefortulsa.org',
    url='https://github.com/codefortulsa/BPZAround.me',
    packages=['bpz'],
    package_dir={'bpz': 'bpz'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='Building planning zoning neighborhoods',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
