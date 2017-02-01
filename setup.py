#!/usr/bin/env python

from setuptools import setup
import subprocess

try:
    import conda.cli
    conda.cli.main('install','--file','requirements.txt')
except Exception as e:
    print(e)

setup(name='pyimagevideo',
	  description='utilites for reading,writing,plotting all kinds of images and video date',
	  author='Michael Hirsch',
	  url='https://github.com/scienceopen/pyimagevideo',
           packages=['pyimagevideo'],
      install_requires=['tifffile'],
	  )
