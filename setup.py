#!/usr/bin/env python
req=['numpy','scipy','scikit-image','matplotlib']
pipreq = ['morecvutils']

import pip
try:
    import conda.cli
    conda.cli.main('install',*req)
except Exception as e:
    import pip
    pip.main(['install'] + req)
pip.main(['install'] + pipreq)
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
      install_requires = req+pipreq,
      extras_require={'tifffiles': ['tifffile']}
	  )
