#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import ezconf

setup(name='ezconf',
      version=ezconf.version,
      description='Yet another JSON configuration file parser',
      url='http://github.com/geosoco/ezconf',
      author='John J Robinson',
      author_email='pubsoco@geosoco.com',
      license='BSD',
      packages=['ezconf'],
      platforms='any',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
      ])