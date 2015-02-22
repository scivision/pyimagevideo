"""
The reason one might use hdf5 instead of TIFF for video-like multi-frame image datasets
is that currently, one can only write a multi-page TIFF using scikit-image freeimage at once.
That is, you can't append frames.
Maybe someone has written a clean TIFF function that can append -- I haven't run across it yet.

"""

import h5py
import numpy as np

x = (np.random.rand(10,512,512)*255).astype(np.uint8)

with h5py.File('/tmp/junk.h5','w',libver='latest') as f:
    dset = f.create_dataset("video", (10,512,512), dtype='uint8')
    print(dset.dtype)