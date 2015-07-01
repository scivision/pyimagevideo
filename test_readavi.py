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
#from warnings import warn


def testreadavi(fn):
    fn = expanduser(fn)
    print(fn)
    vid = cv2.VideoCapture(fn)
    if not vid.isOpened():
        print('could not open '+fn); return

    ret,img = vid.read() #a 3-D Numpy array, last axis is BGR: blue,green,red
    if not ret:
        print('could not read '+fn); return
#%% show first frame with matplotlib (can also do with cv2.imshow(img))
    ax=plt.figure().gca()
    ax.imshow(img[...,::-1],origin='upper') #note flipping of last axis since Matplotlib expects RGB and cv2 is BGR
    ax.set_title(fn,fontsize='small')

    #these two lines are used to make an image update in a loop
    plt.draw()
    plt.pause(0.001)
#%% show first frame with OpenCV
    cv2.imshow('fig1',img) #expects BGR
    cv2.waitKey(0) #this line is necessary to make the image actually be drawn

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='tests OpenCV codec reading of AVI, and displays first frame of file')
    p.add_argument('avifn',help='.avi file you want to read',nargs='?',
                   default='~/U/eng_research_irs/Auroral_Video/X1387_032307_112005.36_short_30fps.avi')
    p = p.parse_args()

    testreadavi(p.avifn)
    #plt.show() #for matplotlib  Not needed if using draw,pause like above