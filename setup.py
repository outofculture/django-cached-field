#!/usr/bin/env python

from __future__ import absolute_import
from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


version = '1.5.0'

setup(name='django-cached-field',
      version=version,
      description="Celery-deferred, cached fields on Django ORM for expensive-to-calculate attributes",
      long_description=readme(),
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='django caching',
      author='Martin Chase',
      author_email='outofculture@gmail.com',
      url='https://github.com/outofculture/django-cached-field',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'django>=1.9',
        'celery>=3.0'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
