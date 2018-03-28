#!/usr/bin/env python
install_requires = ['numpy','scivpy','imageio>=2.3','scikit-image','matplotlib>=2.2']  # skimage needs scipy on Windows
tests_require = ['pytest','nose','coveralls']
# %%
from setuptools import setup,find_packages

setup(name='pyimagevideo',
      packages=find_packages(),
      python_requires='>=3.6',
      install_requires=install_requires,
      extras_require={'tests':tests_require,
                    'io': ['h5py','scipy',
                             'morecvutils'],
                    'audio':[]},
      tests_require=tests_require,
      version='0.6.0',
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/pyimagevideo',
      description='Demos of OpenCV, read/write videos, etc.',
      long_description=open('README.rst').read(),
       classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'Intended Audience :: Education',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Topic :: Multimedia :: Graphics :: 3D Rendering',
      'Topic :: Multimedia :: Graphics :: Presentation',
      'Topic :: Multimedia :: Graphics :: Viewers',
      'Topic :: Multimedia :: Sound/Audio :: Players',
      'Topic :: Scientific/Engineering :: Visualization',
      ],
      include_package_data=True,
	  )
