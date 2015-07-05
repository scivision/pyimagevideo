#!/usr/bin/env python
"""
tests ability of an OpenCV install to read an AVI file
one of the substantial issues with starting to use OpenCV is missing video codecs
tested with OpenCV 2.4
Michael Hirsch
"""
import matplotlib.pyplot as plt
import cv2
from os.path import expanduser
from warnings import warn
#
from getaviprop import getaviprop


def testreadavi(fn):
    fn = expanduser(fn)
    print(fn)
    vid = cv2.VideoCapture(fn)
    if not vid.isOpened():
        print('could not open '+fn); return
    nframe,xpix,ypix,fps,codec = getaviprop(vid)
    print('{} has {} frames at {} fps.'.format(fn,nframe,fps))

    for i in range(nframe-1):
        ret,img = vid.read() #a 3-D Numpy array, last axis is BGR: blue,green,red
        if not ret:
            warn('could not read {} on frame {}'.format(fn,i))
            break
    #show first frame with matplotlib (can also do with cv2.imshow(img))
    #ax=plt.figure().gca()
    #ax.imshow(img[...,::-1],origin='upper') #note flipping of last axis since Matplotlib expects RGB and cv2 is BGR
    #ax.set_title(fn,fontsize='small')

    #these two lines are used to make an image update in a loop
    #plt.draw()
    #plt.pause(0.001)
#%% show video with OpenCV
        cv2.imshow('fig1',img) #expects BGR
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
    #plt.show() #for matplotlib  Not needed if using draw,pause like above