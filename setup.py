#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The howto.05bit.com website
===========================

Run `python setup.py develop` to install dependencies, then
run `docta serve --watch`.
"""
import sys
from setuptools import setup, find_packages

__version__ = '1.0'

# Requirements

install_requires=[
    'docta',
]

# Blacklisted commands

for command in ['register', 'upload']:
    if command in sys.argv:
        values = {'command': command}
        print('Command "%(command)s" has been blacklisted, exiting...' %
              values)
        sys.exit(1)

setup(
    name='howto-05bit',
    version=str(__version__),
    author="Alexey Kinëv",
    author_email='rudy@05bit.com',
    url='https://howto.05bit.com',
    description=__doc__,
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
