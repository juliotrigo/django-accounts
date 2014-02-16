# -*- coding: utf-8 -*-

"""django-accounts setup."""

from __future__ import print_function, unicode_literals

from setuptools import setup, find_packages

import accounts

setup(
    name='accounts',
    version=accounts.__version__,
    author='Julio Vicente Trigo Guijarro',
    author_email='',
    url='http://github.com/juliotrigo/django-accounts/',
    description='A Django app to manage user accounts.',
    long_description=accounts.__doc__,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    license='BSD',
    platforms='any',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
)
