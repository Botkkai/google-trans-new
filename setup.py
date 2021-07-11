#!/usr/bin/env python

from setuptools import setup

setup(
   name='GoogleTrans',
   version='1.0',
   description='A useful module',
   author='Quentin',
   author_email='quentin.sereno3@gmail.com',
   packages=['GoogleTrans'],  #same as name
   install_requires=['requests'], #external packages as dependencies
)
