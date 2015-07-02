.. image:: https://codeclimate.com/github/scienceopen/pyimagevideo/badges/gpa.svg
   :target: https://codeclimate.com/github/scienceopen/pyimagevideo
   :alt: Code Climate

============
pyimagevideo
============

Functions to write multipage images and make videos from Numpy arrays.
Also functions to test Matlab and Python codecs

If you get errors about `libfreeimage. here's how to fix them. <https://scivision.co/writing-multipage-tiff-with-python/>`_

``image_write_multipage.py`` demonstration of writing multipage TIFF from Numpy arrays, using tifffile and freeimage (tifffile is 20x faster and much more featureful)

``imageconv.py`` converts large directory of files with same prefix to multipage TIFFs

``videowritetest.py`` demonstrates using OpenCV to write video, with a lot of codecs to try.

``diric.py`` implementation of Direchlet function in Python, demonstrating optional Numba
