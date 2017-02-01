#!/usr/bin/env python
"""
tests ability of an OpenCV install to read an AVI file
one of the substantial issues with starting to use OpenCV is missing video codecs
tested with OpenCV 2.4
Michael Hirsch
"""
import cv2
from pathlib import Path
#
try:
    from cvutils.getaviprop import getaviprop
except ImportError:
    pass

def testreadavi(fn):
    fn = Path(fn).expanduser()
    vid = cv2.VideoCapture(str(fn))

    try:
        vparam = getaviprop(vid)
        print(vparam)
    except Exception:
        pass

    while True:
        ret,img = vid.read() #a 3-D Numpy array, last axis is BGR: blue,green,red
        if not ret: #end of file
            break
#%% show video with OpenCV
        cv2.imshow(str(fn),img) #expects BGR
        cv2.waitKey(delay=1) #this line is necessary to make the image actually be drawn
#%% cleanup
    vid.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='tests OpenCV codec reading of AVI, and displays first frame of file')
    p.add_argument('avifn',help='.avi file you want to read')
    p = p.parse_args()

    testreadavi(p.avifn)
