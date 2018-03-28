#%% using libtiff
def rwlibtiff(x,fn):
    """
    It seems with verion 0.4.0 that it requires Python 2.7, but I get a
    segmentation fault even with Python 2.7
    """
    from libtiff import TIFFimage, TIFF
    with TIFFimage(x,description='my test data') as tf:
        print(f'libtiff write {fn}')

        #write demo
        tf.write_file(str(fn), compression='none')

    #read demo
    with TIFF.open(str(fn),mode='r') as tif:

        return tif.read_image()
        # for image in tif.iter_images():

# %% tifffile
    if 'tifffile' in modules:
        ofn = mkstemp('.tif','tifffile')[1]

        tic = time()
        write_multipage_tiff(imgs, ofn,
                             descr='0 to 9 numbers',
                             tags=[(65000,'s',None,'My custom tag #1',True),
                                   (65001,'s',None,'My custom tag #2',True),
                                   (65002,'f',2,[123456.789,9876.54321],True)])
        y = read_multipage_tiff(ofn)
        print(f'{time()-tic:.6f} seconds to read/write {ofn} with tifffile.')
        assert (y==imgs).all(),'tifffile read/write equality failure'

        # %%
    if 'libtiff' in modules:
        tic = time()
        ofn = mkstemp('.tif','libtiff')[1]
        y = rwlibtiff(imgs, ofn)
        print(f'{time()-tic:.6f} seconds to read/write {ofn} with libtiff.')
        assert (y==imgs).all(),'libtiff read/write equality failure'
    return y


#%% using tifffile
def write_multipage_tiff(x,ofn,descr=None,tags=()):
    """ uses ZIP compression
    writes all frames at once
    note: using TiffWriter class, you can
    APPEND write TIFF FRAME BY FRAME
    see source code for more detail, search for
    class TiffWriter
    https://github.com/blink1073/tifffile/blob/master/tifffile.py
    """
    logging.debug('write_mulitpage_tiff: description to write: {}'.format(descr))

    tifffile.imsave(str(ofn),x,compress=6,
                        #photometric='minisblack', #not for color
                        description=descr,
                        extratags=tags)


def read_multipage_tiff(fn,verbose=False):
    with tifffile.TiffFile(str(fn)) as tif:
        y = tif.asarray()
        if verbose:
            loadtifftags(tif)
    return y