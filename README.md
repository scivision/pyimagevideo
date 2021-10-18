# Python Image and Video Read/Write Examples

[![DOI](https://zenodo.org/badge/30741849.svg)](https://zenodo.org/badge/latestdoi/30741849)
[![Actions Status](https://github.com/scivision/pyimagevideo/workflows/ci/badge.svg)](https://github.com/scivision/pyimagevideo/actions)
[![PyPi Download stats](http://pepy.tech/badge/pyimagevideo)](http://pepy.tech/project/pyimagevideo)

Functions to **write multipage images** and **make videos** from Numpy arrays.
Also includes functions to test Matlab and Python OpenCV codecs.

```sh
python -m pip install -e .
```

[HDF5_to_AVI.py](./HDF5_to_AVI.py) converts HDF5 video data to AVI.
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

* errors: `libfreeimage`, how to fix them: https://www.scivision.dev/writing-multipage-tiff-with-python/
