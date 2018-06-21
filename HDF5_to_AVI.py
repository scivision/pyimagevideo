#!/usr/bin/env python
"""
Note: VideoWriter expects dimensions (x,y,3) and will fail otherwise,writing a tiny file perhaps
Remember, VLC has a long-standing bug where files under about 3fps don't playback

Note: the isColor parameter of VideoWriter works on Linux too

Example:
./Convert_HDF5_to_AVI.py ~/data/2012-12-25/extracted.h5 -o ~/data/2012-12-25/ex.ogv -cc4 THEO

Just get percentiles
./Convert_HDF5_to_AVI.py ~/data/2012-12-25/extracted.h5

"""
import sys
import logging
from pathlib import Path
import h5py
import numpy as np
from typing import List, Any
# from scipy.misc import bytescale BUGS
# from scipy.signal import wiener

from histutils import sixteen2eight
from pyimagevideo import VideoWriter
sys.tracebacklimit = 1

usecolor = False
PTILE = [5, 99.95]
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


def hdf2avi(infn: Path, outfn: Path,
            h5key: str, cc4: str,
            mm=None, fps=None,
            ptile=PTILE, step=1):
    """
    infn: HDF5 file containing video to read
    outfn: video file
    h5key: HDF5 path to video. Assuming shape Nframe x Y x X x 3 (RGB color)  or Nframe x Y x X  (gray)
    """
    if h5key is None:
        return

    window = step * 100  # number of frames over which to auto contrast

    infn = Path(infn).expanduser()
    outfn = Path(outfn).expanduser()

    assert infn.is_file(), f'{infn} is not a file'
    assert outfn.suffix in ('.ogv', '.mkv', '.avi')

    if cc4 == 'THEO':
        assert outfn.suffix == '.ogv'

    if outfn.is_file():
        raise IOError(f'video output {outfn} already exists.')
# %% open HDF5 video for parameters
    with h5py.File(infn, 'r') as f:
        N, y, x = f[h5key].shape[:3]
        Next = N // step
        print(f'converting {Next} / {N} frames sized {x} x {y} from {infn} to {outfn}')
# %% initialize OpenCV video writer
        if N < 100:
            print(f'picking FPS=4, lossless codec FFV1 due to small amount Nframe {N}')
            fps = 4
            outfn.with_suffix('.avi')
            cc4 = 'FFV1'
            window = step * Next // 10
        elif fps is None:
            fps = 20

        if fps <= 3:
            logging.warning('FPS<=3 might not work with some AVI players e.g. VLC')

        h: Any = VideoWriter(outfn, cc4, (x, y), fps, usecolor)
# %% loop over HDF5 video
        for i in range(0, N, step):
            if not i % window:
                if mm is None:
                    minmax = np.percentile(f[h5key][i:i + window:step, :, :], ptile, interpolation='nearest')
                else:
                    minmax = mm

                if minmax[0] != minmax[1]:
                    print(f'{i/N*100:.1f} %  min/max {minmax}\r', end="")
                else:
                    logging.error(f'{i/N*100:.1f} %  Min==max no input image contrast')

            im = f[h5key][i, :, :]
            # I = wiener(I,wienernhood)
            # img = bytescale(I, minmax[0], minmax[1]) BUG
            img = sixteen2eight(im, minmax)
            h.write(img)
# %% close video
    h.release()


def getprc(fn: Path, key: str, stride: int=60, ptile: List[float]=PTILE):
    """ plot some file statistics to help decide min/max"""
    fn = Path(fn).expanduser()
    fGB = fn.stat().st_size / 1e9
    print(f'sampling {ptile} percentiles {fn}, reading {1/stride*fGB:.1f} of {fGB:.1f} GB')

    with h5py.File(fn, 'r') as f:
        prc = np.percentile(f[key][::stride, ...], ptile, interpolation='nearest')

    print(f'percentiles {ptile}:  {prc}')


def findvidvar(fn: Path):
    """
    assumes which variable is video in an HDF5 file
    by finding variable of larget size (number of elements) in an HDF5 file that's 3-D or 4-D
    """
    fn = Path(fn).expanduser()

    x = {}
    with h5py.File(fn, 'r') as f:
        for v in f:
            if f[v].ndim in (3, 4):
                x[v] = f[v].size

    vid = max(x, key=x.get)
    print(f'using "{vid}" as video variable in {fn}')
    return vid


if __name__ == '__main__':
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('infn', help='HDF5 video file to read')
    p.add_argument('outfn', help='video file to write e.g. cool.avi')
    p.add_argument('-k', '--h5key', help='key to HDF5 video (variable in HDF5 file)')
    p.add_argument('-cc4', help='video codec CC4 code', default='FMP4')
    p.add_argument('-minmax', help='minimum, maximum values. Automatic if not specified.')
    p.add_argument('-fps', help='frames/sec of output video', type=int, default=None)
    p.add_argument('-s', '--step', help='take every Nth frame (default 1)', type=int, default=1)
    P = p.parse_args()

    h5key = findvidvar(P.infn) if P.h5key is None else P.h5key

    if not P.outfn:
        getprc(P.infn, h5key)
    else:
        hdf2avi(P.infn, P.outfn, h5key, P.cc4, P.minmax, P.fps, step=P.step)
