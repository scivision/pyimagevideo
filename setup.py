#!/usr/bin/env python
install_requires = ['numpy','scipy','imageio','tifffile','matplotlib']
tests_require = ['nose','coveralls']
# %%
from setuptools import setup,find_packages

setup(name='pyimagevideo',
      packages=find_packages(),
      python_requires='>=3.6',
      install_requires=install_requires,
      extras_require={'tests':tests_require,
                    'io': ['h5py','scikit-image',
                             'morecvutils']},
      tests_require=tests_require,
      version='0.6.0',
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/pyimagevideo',
      description='Demos of OpenCV, read/write videos, etc.',
       classifiers=[
      'Development Status :: 4 - Beta',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      ],
	  )
