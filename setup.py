#!/usr/bin/env python
req=['numpy','scipy']
# %%
from setuptools import setup

setup(name='pyimagevideo',
      packages=['pyimagevideo'],
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/pyimagevideo',
      description='Demos of OpenCV, read/write videos, etc.',
       classifiers=[
      'Development Status :: 4 - Beta',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      ],
      install_requires = req,
      python_requires='>=3.6',
      extras_require={'io': ['h5py','scikit-image','matplotlib','tifffile',
                             'morecvutils']}
	  )
