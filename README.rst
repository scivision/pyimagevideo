.. image:: https://travis-ci.org/scienceopen/pyimagevideo.svg?branch=master
    :target: https://travis-ci.org/scienceopen/pyimagevideo
.. image:: https://coveralls.io/repos/github/scienceopen/pyimagevideo/badge.svg?branch=master 
    :target: https://coveralls.io/github/scienceopen/pyimagevideo?branch=master

============
pyimagevideo
============

Functions to **write multipage images** and **make videos** from Numpy arrays.
Also includes functions to test Matlab and Python codecs

If you get errors about `libfreeimage, here's how to fix them. <https://scivision.co/writing-multipage-tiff-with-python/>`_

``image_write_multipage.py`` demonstration of writing multipage TIFF from Numpy arrays, using tifffile and freeimage (tifffile is 20x faster and much more featureful)

``imageconv.py`` converts large directory of files with same prefix to multipage TIFFs

Python lossless AVI writing
===========================
You can write AVI from Python without axes labels (openCV) or with labels/axes (Matplotlib)

`Demo_OpenCV_writeAVI.py <Demo_OpenCV_writeAVI.py>`_ demonstrates using OpenCV to write video, with a lot of codecs to try. This does not insert any of the axes stuff that Matplotlib does, so it can be useful for machine vision work. You can optinally overlay dynamic text on the video.

`matplotlib_avi.py <matplotlib_avi.py>`_ writes axes labels AVIs lossless using Matplotlib
