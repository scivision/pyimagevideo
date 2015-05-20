#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program tests writing multipage TIFF using three different TIFF modules
also demonstrates writing/reading custom user TIFF tags with Python
Michael Hirsch
At this time, I prefer tifffile

Notes on custom tags:
TIFF 6.0 specification page 8
http://partners.adobe.com/public/developer/en/tiff/TIFF6.pdf
says:
"Do not choose your own tag numbers. Doing so could cause serious compatibility
problems in the future. However, if there is little or no chance that your TIFF files
will escape your private environment, please consider using TIFF tags in the
“reusable” 65000-65535 range. You do not need to contact Adobe when using
numbers in this range."

reference: http://www.digitalpreservation.gov/formats/content/tiff_tags.shtml
"""
from tempfile import gettempdir
from os.path import join
from numpy import random, uint8
from time import time
try:
    from skimage.io._plugins import freeimage_plugin as freeimg
    from skimage.io import imread as skimread
except ImportError as e:
    print(e)
try:
    import tifffile
except ImportError as e:
    print(e)

def tiffdemo(modules):
#%% test parameters
    nframe=10
    tdir = gettempdir()
#%% generate synthetic multiframe image
    x = (random.rand(nframe,512,512,3)*255).astype(uint8)

    if 'tifffile' in modules:
        ofn = join(tdir,'tifffile.tif')
        tic = time()
        write_multipage_tiff(x,ofn,descr='my random data',
                             tags=[(65000,'s',None,'My custom tag #1',True),
                                   (65001,'s',None,'My custom tag #2',True),
                                   (65002,'f',2,[123456.789,9876.54321],True)])
        y = read_multipage_tiff(ofn)
        print('{:.2f} seconds to read/write with tiffile.'.format(time()-tic))

    if 'freeimage' in modules:
        ofn = join(tdir,'freeimage.tif')
        tic = time()
        write_multipage_freeimage(x,ofn)
        y = skimread(ofn)
        print('{:.2f} seconds to read/write with freeimage.'.format(time()-tic))

    if 'libtiff' in modules:
        tic = time()
        y = rwlibtiff(x,join(tdir,'testlibtiff.tif'))
        print('{:.2f} seconds to read/write with libtiff.'.format(time()-tic))

    return y

#%% using tifffile
def write_multipage_tiff(x,ofn,descr='',tags=None):
    """ uses ZIP compression
    writes all frames at once
    note: using TiffWriter class, you can
    APPEND write TIFF
    FRAME BY FRAME
    see source code for more detail, search for
    class TiffWriter
    https://github.com/blink1073/tifffile/blob/master/tifffile.py
    """
    try:
        tifffile.imsave(ofn,x,compress=6,
                        #photometric='minisblack', #not for color
                        description=descr,
                        extratags=tags)

    except Exception as e:
        print('tifffile had a writing problem with {}   {} '.format(ofn,e))

def read_multipage_tiff(ofn):
    #read demo
    try:
        with tifffile.TiffFile(ofn) as tif:
            y = tif.asarray()
            for page in tif:
                for tag in page.tags.values():
                    t = tag.name, tag.value
                    if tag.name in ('65000','65001','65002'):
                        print(t)
        return y
    except Exception as e:
        print('tifffile had a reading problem with {}   {} '.format(ofn,e))
#%% demo writing TIFF using scikit-image and free image
def write_multipage_freeimage(x,ofn):
    """
    uses LZW compression for TIFF, but is far slower (20x) than tifffile
    writes bad/corrupt/weird multipage GIF
    """
    try:
        print('freeimage write {}   shape {}'.format(ofn,x.shape))
        #write demo (no tags)
        freeimg.write_multipage(x, ofn)
    except Exception as e:
        print('freeimage had a problem: '+str(e))
        print('https://scivision.co/writing-multipage-tiff-with-python/')
#%% using libtiff
def rwlibtiff(x,fn):
    """
    It seems with verion 0.4.0 that it requires Python 2.7, but I get a
    segmentation fault even with Python 2.7
    """
    try:
        from libtiff import TIFFimage, TIFF
        with TIFFimage(x,description='my test data') as tf:
            print('libtiff write ' + fn)

            #write demo
            tf.write_file(fn, compression='none')

        #read demo
        with TIFF.open(fn,mode='r') as tif:

            return tif.read_image()
            # for image in tif.iter_images():
    except Exception as e:
        print('libtiff had a problem: ' + str(e))

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='demo of different TIFF modules read/write with custom user tags')
    p.add_argument('module',help='module to use: (tifffile, freeimage, libtiff) default: tifffile',nargs='?',default=('tifffile','freeimage'))
    p=p.parse_args()

    y = tiffdemo(p.module)

    try:
        print(y.shape)
        from matplotlib.pyplot import figure,show
        ax = figure().gca()
        ax.imshow(y[0,...])
        show()
    except Exception as e:
        print(e)
        print('could not plot result, sorry')
