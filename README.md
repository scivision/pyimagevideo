[![Code Climate](https://codeclimate.com/github/scienceopen/pyimagevideo/badges/gpa.svg)](https://codeclimate.com/github/scienceopen/pyimagevideo)

# python-test-functions
Functions to test various packages installed.

You'll need [libfreeimage](https://scivision.co/writing-multipage-tiff-with-python/)

``` image_write_multipage.py ``` demonstration of writing multipage TIFF from Numpy arrays, using tifffile and freeimage (tifffile is 20x faster and much more featureful)

``` imageconv.py ``` converts large directory of files with same prefix to multipage TIFFs

``` videowritetest.py ``` demonstrates using OpenCV to write video, with a lot of codecs to try.

``` diric.py ``` implementation of Direchlet function in Python, demonstrating optional Numba
