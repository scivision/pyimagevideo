#!/usr/bin/env python
"""
Note: VideoWriter expects dimensions (x,y,3) and will fail otherwise,writing a tiny file perhaps
Remember, VLC has a long-standing bug where files under about 3fps don't playback

Note: the isColor parameter of VideoWriter works on Linux too

Example:
./Convert_HDF5_to_AVI.py ~/data/2012-12-25/extracted.h5 ~/data/2012-12-25/ex.ogv THEO -minmax 30 2000

Just get percentiles
./Convert_HDF5_to_AVI.py ~/data/2012-12-25/extracted.h5

"""
from pathlib import Path
import h5py
import numpy as np
from scipy.misc import bytescale
#
from pyimagevideo import videoWriter

usecolor = False

"""
all of these codecs worked for me on Ubuntu 14.04 and 16.04
'MJPG' Motion JPEG
'XVID' MPEG-4
'FFV1' Lossless
'FMP4' MPEG-4

** maybe works somewhat
'THEO' ext='.ogv' #must name file .ogv, NOT .avi\  -- somewhat broken, per messages in ffplay

*** NOT working for me on Ubuntu 16.04 ***
'YV12'
'IYUV'
'Y41P' #silent error, no write
'YUV9' #silent error, no write -- 15.04 writes but nobody knows how to play
'DIB ' # silent error, no write
'CVID' #encoder not found
'MJ2C' #segmentation fault -- 15.04 blank video
"""

def hdf2avi(infn:Path, outfn:Path, h5key:str, cc4:str, mm,fps):
    """
    infn: HDF5 file containing video to read
    outfn: video file
    h5key: HDF5 path to video. Assuming shape Nframe x Y x X x 3 (RGB color)  or Nframe x Y x X  (gray)
    """
    infn = Path(infn).expanduser()
    outfn = Path(outfn).expanduser()

    if cc4=='THEO':
        assert outfn.suffix=='.ogv'
# %% open HDF5 video for parameters
    with h5py.File(infn,'r',libver='latest') as f:
        N,y,x = f[h5key].shape[:3]
        print('converting {} frames sized {}x{} from {} to {}'.format(N,x,y,infn,outfn))
# %% initialize OpenCV video writer
        h = videoWriter(outfn, cc4, (x, y), fps, usecolor)
# %% loop over HDF5 video
        for i,I in enumerate(f[h5key]):
            if not i % 100:
                print('{:.1f} %'.format(i/N*1000))
            img = bytescale(I, mm[0], mm[1])
            h.write(img)
# %% close video
    h.release()

def getprc(fn,key,stride=60,ptile=[.01,99.999]):
    """ plot some file statistics to help decide min/max"""
    fn = Path(fn).expanduser()
    fGB = fn.stat().st_size/1e9
    print(f'sampling {ptile} percentiles {fn}, reading {1/60*fGB:.1f} of {fGB:.1f} GB')

    with h5py.File(fn,'r',libver='latest') as f:
        prc = np.percentile(f[key][::stride,...],ptile,interpolation='nearest')

    print(f'percentiles {ptile}:  {prc}')

def findvidvar(fn):
    """
    assumes which variable is video in an HDF5 file
    by finding variable of larget size (number of elements) in an HDF5 file that's 3-D or 4-D
    """
    fn = Path(fn).expanduser()
    x = {}
    with h5py.File(fn,'r') as f:
         for v in f:
             if f[v].ndim in (3,4):
                 x[v] = f[v].size

    vid = max(x,key=x.get)
    print(f'using "{vid}" as video variable in {fn}')
    return vid


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('infn',help='HDF5 video file to read')
    p.add_argument('-o','--outfn',help='video file to write e.g. cool.avi')
    p.add_argument('-k','--h5key',help='key to HDF5 video (variable in HDF5 file)')
    p.add_argument('cc4',help='video codec CC4 code',nargs='?',default='FMP4')
    p.add_argument('-minmax',help='minimum, maximum values. default (0,65535)',type=int,nargs=2,default=(0,65535))
    p.add_argument('-fps',help='frames/sec of output video',type=int,default=20)
    p = p.parse_args()

    h5key = findvidvar(p.infn) if p.h5key is None else p.h5key

    if not p.outfn:
        getprc(p.infn, h5key)
    else:
        hdf2avi(p.infn, p.outfn, h5key, p.cc4, p.minmax,p.fps)