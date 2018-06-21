 [![Travis CI status](https://travis-ci.org/scivision/pyimagevideo.svg?branch=master)](https://travis-ci.org/scivision/pyimagevideo)
[![coverage](https://coveralls.io/repos/github/scivision/pyimagevideo/badge.svg?branch=master)](https://coveralls.io/github/scivision/pyimagevideo?branch=master)
[![AppVeyor CI](https://ci.appveyor.com/api/projects/status/b55xigknwgd8m0y7?svg=true)](https://ci.appveyor.com/project/scivision/pyimagevideo)
[![Maintainability](https://api.codeclimate.com/v1/badges/f9bdbab86e37a3680cfe/maintainability)](https://codeclimate.com/github/scivision/pyimagevideo/maintainability)
[![pypi versions](https://img.shields.io/pypi/pyversions/pyimagevideo.svg)](https://pypi.python.org/pypi/pyimagevideo)
[![pypi format](https://img.shields.io/pypi/format/pyimagevideo.svg)](https://pypi.python.org/pypi/pyimagevideo)
[![PyPi Download stats](http://pepy.tech/badge/pyimagevideo)](http://pepy.tech/project/pyimagevideo)

# Python Image and Video Read/Write Examples

Functions to **write multipage images** and **make videos** from Numpy arrays. 
Also includes functions to test Matlab and Python OpenCV codecs.

## Install

    python -m pip install -e .

## Scripts


`Convert_HDF5_to_AVI.py` converts HDF5 video data to AVI. 
Typically used in biomedical and science imaging, where they use HDF5 instead of TIFF,
since HDF5 is a very widespread, fast file format that can store arbitrarily large datasets and metadata. 
It is recommended to researchers to use HDF5 instead of TIFF, FITS, CDF or proprietary
formats for large data streams, including lossless video.

`image_write_multipage.py` demonstration of writing multipage TIFF from
Numpy arrays, using `tifffile` and freeimage (tifffile is 20x faster and
much more featureful)

`imageconv.py` converts large directory of files with same prefix to multipage TIFFs

## Audio

The `audio_*.py` scripts show several methods for generating audio
output from Python.

## Python lossless AVI writing

You can write AVI from Python without axes labels (openCV) or with labels/axes (Matplotlib)

### OpenCV AVI writing

[Demo_OpenCV_writeAVI.py](Demo_OpenCV_writeAVI.py) demonstrates using
OpenCV to write video, with a lot of codecs to try. This does not insert
any of the axes stuff that Matplotlib does, so it can be useful for
machine vision work. You can optinally overlay dynamic text on the
video.

### Matplotlib AVI writing

[matplotlib_writeavi.py](matplotlib_writeavi.py) writes axes labels
AVIs lossless using Matplotlib. Note that file-based
`matplotlib.animation.writers['ffmpeg_file']` is used for better
reliability, even though it takes twice as long as the pipe-based
`ffmpeg`. On some computers, pipe-based
`matplotlib.animation.writers['ffmpeg']` results in very distorted,
scrambled output for some reason, with Matplotlib 1.5 and 2.0. In that
case, I have empirically found `ffmpeg_file` to Just Work.

## Notes

-   errors: `libfreeimage`, how to fix them: https://www.scivision.co/writing-multipage-tiff-with-python/

