#!/usr/bin/env python3

from setuptools import setup
import subprocess

with open('README.rst','r') as f:
	long_description = f.read()

setup(name='pyimagevideo',
      version='0.1',
	  description='utilites for reading,writing,plotting all kinds of images and video date',
	  long_description=long_description,
	  author='Michael Hirsch',
	  url='https://github.com/scienceopen/pyimagevideo',
           packages=['pyimagevideo'],
      install_requires=['tifffile'],
	  )

try:
    subprocess.call(['conda','install','--yes','--quiet','--file','requirements.txt'],shell=False) #don't use os.environ
except Exception as e:
    print('you will need to install packages in requirements.txt  {}'.format(e))
