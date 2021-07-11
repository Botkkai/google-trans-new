#!/usr/bin/env python

from setuptools import setup

setup(
   name='google_trans_new',
   version='1.0',
   description='A useful module',
   author='Quentin',
   author_email='quentin.sereno3@gmail.com',
   packages=['google_trans_new'],  #same as name
   install_requires=['requests'], #external packages as dependencies
)
