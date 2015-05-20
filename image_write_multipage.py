#!/usr/bin/env python3
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

def tiffdemo(modules):
#%% test parameters
    nframe=10
    tdir = gettempdir()
#%% generate synthetic multiframe image
    x = (random.rand(nframe,512,512)*255).astype(uint8)
    
    if 'tifffile' in modules:
        y = rwtifffile(x,tdir)
        
    if 'freeimage' in modules:
        y = rwfreeimage(x,tdir)
    
    if 'libtiff' in modules:
        y = rwlibtiff(x,tdir)
        
    return y

#%% using tifffile
def rwtifffile(x,tdir):
    """ uses ZIP compression
    note: using TiffWriter class, you can append write TIFF frame by frame  
    see source code for more detail, search for 
    class TiffWriter
    https://github.com/blink1073/tifffile/blob/master/tifffile.py
    """
    try:
        import tifffile
        fn = join(tdir,'tifffile.tif'); print('tifffile write ' + fn)
    
        #write demo
        tifffile.imsave(fn,x,compress=6, 
                        photometric='minisblack',
                        description='my random data',
                        extratags=[(65000,'s',None,'My custom tag #1',True),
                                   (65001,'s',None,'My custom tag #2',True),
                                   (65002,'f',2,[123456.789,9876.54321],True)])
        #read demo
        with tifffile.TiffFile(fn) as tif:
            y = tif.asarray()
            for page in tif:
                for tag in page.tags.values():
                    t = tag.name, tag.value
                    if tag.name in ('65000','65001','65002'):
                        print(t)
        
    except Exception as e:
        print('tifffile had a problem: ' + str(e))
        #raise
    return y
    
#%% demo writing TIFF using scikit-image and free image
def rwfreeimage(x,tdir):
    """ on my setup, uses LZW compression """
    try:
        from skimage.io._plugins import freeimage_plugin as freeimg
        from skimage.io import imread as skimread
        fn = join(tdir,'freeimage.tif'); print('freeimage write ' + fn)
        
        #write demo (no tags)        
        freeimg.write_multipage(x, fn)
        
        #read demo (no tags)
        return skimread(fn)
    except Exception as e:
        print('freeimage had a problem: '+str(e))
    
#%% using libtiff
def rwlibtiff(x,tdir):
    """ I get an error "no module name libtiff"""
    try:
        from libtiff import TIFFimage, TIFF
        with TIFFimage(x,description='my test data') as tf:
            fn = join(tdir,'.tif'); print('libtiff write ' + fn)
            
            #write demo
            tf.write_file(fn, compression='none')
            
        #read demo  
        with TIFF.open(fn,mode='r') as tif:
            
            y = tif.read_image()
            # for image in tif.iter_images():
    except Exception as e:
        print('libtiff had a problem: ' + str(e))
        #raise
    
    return y    
    
if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='demo of different TIFF modules read/write with custom user tags')
    p.add_argument('module',help='module to use: (tifffile, freeimage, libtiff) default: tifffile',nargs='?',type=str,default='tifffile')
    a=p.parse_args()
    
    y = tiffdemo(a.module)
    
    try:
        print(y.shape)
        from matplotlib.pyplot import figure,show
        ax = figure().gca()
        ax.imshow(y[0,...])
        show()        
    except Exception as e:
        print(e)
        print('could not plot result, sorry')
