#!/usr/bin/env python
"""
read an AVI and do LBP on it
"""
from pathlib import Path
import cv2 #used to read AVI and for high-speed display
from skimage.feature import local_binary_pattern
#
#from cvutils.getaviprop import getaviprop

def demoLBP(fn):
    fn = Path(fn).expanduser()
    vid = cv2.VideoCapture(str(fn))
#    vidparam = getaviprop(vid)

    while True:
        ret,img = vid.read()
        if not ret:
            break
        if img.ndim==3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        lbp = local_binary_pattern(img,8,3,'default')
        cv2.imshow('lbp',lbp)
        cv2.waitKey(delay=1)

if __name__ == '__main__':
    from argparse import ArgumentParser
    p= ArgumentParser(description='load avi and demo LBP alg.')
    p.add_argument('avifn',help='.avi file to process')
    p = p.parse_args()

    demoLBP(p.avifn)
