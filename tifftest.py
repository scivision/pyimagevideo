#!/usr/bin/env python3
"""
This program tests writing multipage TIFF using a few different TIFF modules
Michael Hirsch
"""
from tempfile import gettempdir
tdir = gettempdir()
from os.path import join
#%% test parameters
nframe=10
#%% generate synthetic multiframe image
from numpy import random, uint8
x = (random.rand(nframe,512,512)*255).astype(uint8)
#%% using scikit-image and free image
""" on my setup, uses LZW compression """
try:
    from skimage.io._plugins import freeimage_plugin as freeimg
    freeimfn = join(tdir,'freeimage.tif'); print('freeimage write ' + freeimfn)
    freeimg.write_multipage(x, freeimfn)
except Exception as e:
    print('freeimage had a problem: '+str(e))
#%% using tifffile
""" uses ZIP compression """
try:
    import tifffile
    tffn = join(tdir,'tifffile.tif'); print('tifffile write ' + tffn)
    tifffile.imsave(tffn,x,compress=6)
except Exception as e:
    print('tifffile had a problem: ' + str(e))
#%% using libtiff
""" I get an error "no module name libtiff"""
try:
    from libtiff import TIFFimage
    with TIFFimage(x,description='my test data') as tf:
        ltfn = join(tdir,'.tif'); print('libtiff write ' + ltfn)
        tf.write_file(ltfn, compression='none')
except Exception as e:
    print('libtiff had a problem: ' + str(e))
    raise