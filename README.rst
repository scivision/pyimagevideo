.. image:: https://travis-ci.org/scivision/pyimagevideo.svg?branch=master
    :target: https://travis-ci.org/scivision/pyimagevideo
.. image:: https://coveralls.io/repos/github/scivision/pyimagevideo/badge.svg?branch=master 
    :target: https://coveralls.io/github/scivision/pyimagevideo?branch=master

============
pyimagevideo
============

.. contents::

Functions to **write multipage images** and **make videos** from Numpy arrays.
Also includes functions to test Matlab and Python codecs

``Convert_HDF5_to_AVI.py`` converts HDF5 video data to AVI.
Typically used in biomedical and science imaging, where they use HDF5 instead of TIFF, since HDF5 is a very widespread, fast file format that can store arbitrarily large datasets and metadata.  
It is recommended to researchers to use HDF5 instead of TIFF, FITS, CDF or proprietary formats for large data streams, including lossless video.

``image_write_multipage.py`` demonstration of writing multipage TIFF from Numpy arrays, using ``tifffile`` and freeimage (tifffile is 20x faster and much more featureful)

``imageconv.py`` converts large directory of files with same prefix to multipage TIFFs

Python lossless AVI writing
===========================
You can write AVI from Python without axes labels (openCV) or with labels/axes (Matplotlib)

OpenCV AVI writing
------------------

`Demo_OpenCV_writeAVI.py <Demo_OpenCV_writeAVI.py>`_ demonstrates using OpenCV to write video, with a lot of codecs to try. This does not insert any of the axes stuff that Matplotlib does, so it can be useful for machine vision work. You can optinally overlay dynamic text on the video.

Matplotlib AVI writing
----------------------

`matplotlib_writeavi.py <matplotlib_writeavi.py>`_ writes axes labels AVIs lossless using Matplotlib.
Note that file-based ``matplotlib.animation.writers['ffmpeg_file']`` is used for better reliability, even though it takes twice as long as the pipe-based ``ffmpeg``.
On some computers, pipe-based ``matplotlib.animation.writers['ffmpeg']`` results in very distorted, scrambled output for some reason, with Matplotlib 1.5 and 2.0. 
In that case, I have empirically found ``ffmpeg_file`` to Just Work.

Notes
=====

* errors: ``libfreeimage``, how to fix them: <https://www.scivision.co/writing-multipage-tiff-with-python/>`_

