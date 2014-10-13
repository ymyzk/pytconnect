#!/usr/bin/env python

import sys

from setuptools import setup


__author__ = 'Yusuke Miyazaki <miyazaki.dev@gmail.com>'
__version__ = '0.1'

requires = []

if sys.version_info < (3, 4):
    requires.append('enum34>=1.0')

setup(
    name='pytconnect',
    version=__version__,
    author=__author__,
    author_email='miyazaki.dev@gmail.com',
    description='Tools for analyzing iTunes Connect sales report files',
    packages=['pytconnect'],
    test_suite='tests',
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python'
    ]
)