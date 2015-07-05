#!/usr/bin/env python3
"""
read an AVI and do LBP on it
"""
import cv2 #used to read AVI and for high-speed display
from skimage.feature import local_binary_pattern
from warnings import warn
#
from getaviprop import getaviprop

def demoLBP(fn):

    vid = cv2.VideoCapture(fn)
    nframe,xpix,ypix,fps,codec = getaviprop(vid)

    for i in range(nframe):
        ret,img = vid.read()
        if not ret:
            warn('problem reading {}'.format(fn))
            break
        lbp = local_binary_pattern(img,8,3,'default')
        cv2.imshow('lbp',lbp)
        cv2.waitKey(delay=1)

if __name__ == '__main__':
    from argparse import ArgumentParser
    p= ArgumentParser(description='load avi and demo LBP alg.')
    p.add_argument('avifn',help='.avi file to process')
    p = p.parse_args()

    demoLBP(p.avifn)