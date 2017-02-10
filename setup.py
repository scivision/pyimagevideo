#!/usr/bin/env python
from setuptools import setup

req=['tifffile',
    'numpy','scikit-image','matplotlib']

setup(name='pyimagevideo',
      packages=['pyimagevideo'],
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scienceopen/pyimagevideo',
      description='Demos of OpenCV, read/write videos, etc.',
       classifiers=[
      'Development Status :: 4 - Beta',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3.6',
      ],
      setup_requires=['numpy'], #for tifffile
      install_requires=req,
	  )
