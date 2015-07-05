#!/usr/bin/env python3
"""
gets basic info about AVI file using OpenCV

input: filename or cv2.Capture
"""
import cv2
from cv2 import cv
from numpy import int64
from warnings import warn
from six import string_types,integer_types
from os.path import isfile


def getaviprop(f):
    if isinstance(f,string_types): #assuming filename
        if isfile(f):
            v = cv2.VideoCapture(f)
        else:
            warn('{} does not exist'.format(f))
            return (None,)*5
    else: #assuming cv2.VideoCapture object
        v=f

    if not v.isOpened():
        warn('cannot read {}  probable codec issue'.format(f))
        return (None,)*5

    nframe = int64(v.get(cv.CV_CAP_PROP_FRAME_COUNT))
    xpix = int(v.get(cv.CV_CAP_PROP_FRAME_WIDTH))
    ypix = int(v.get(cv.CV_CAP_PROP_FRAME_HEIGHT))
    fps  = v.get(cv.CV_CAP_PROP_FPS)
    codec= fourccint2ascii(int(v.get(cv.CV_CAP_PROP_FOURCC)))

    if isinstance(f,string_types): #not if it was fed a capture!
        v.release()

    return nframe,xpix,ypix,fps,codec

def fourccint2ascii(fourcc_int):
    """
    useful for converting fourcc in integer form (32-bit int) to ASCII
    """
    assert isinstance(fourcc_int,integer_types)
    fourcc_bin = bin(fourcc_int)
    if len(fourcc_bin) != 32:
        raise ValueError('len(fourcc_bin) = {}   may need zero padding'.format(len(fourcc_bin)))
    fourcc = ''
    for i in range(4):
        fourcc += chr(int(fourcc_bin[i*8:(i+1)*8],2)).replace('\x00',' ')
    return fourcc

if __name__ == '__main__':
    from argparse import ArgumentParser
    p=ArgumentParser(description='get parameters of AVI file')
    p.add_argument('avifn',help='avi filename')
    p=p.parse_args()

    nframe,xpix,ypix,fps,codec = getaviprop(p.avifn)
    if nframe is not None:
        print('{} has {} frames at {} fps, and {} x {} pixels, using the {} codec.'.format(p.avifn,nframe,fps,xpix,ypix,codec))