#!/usr/bin/python2
"""
Note: VideoWriter expects dimensions (x,y,3) and will fail otherwise,writing a tiny file perhaps
Remember, VLC has a long-standing bug where files under about 3fps don't playback

Note: the isColor parameter of VideoWriter works on Linux!
"""
import cv2
try:
    from cv2.cv import FOURCC as fourcc #Windows needs from cv2.cv
except ImportError:
    from cv2 import VideoWriter_fourcc as fourcc

import numpy as np
from tempfile import gettempdir
from os.path import join

usecolor = False
nframe=100
xpix=ypix=256

ext='.avi'
#*** all of these codecs worked for me on Ubuntu 14.04 and 15.04***
cc4 = fourcc(*'MJPG') #works in 15.04,14.04 plays wherever
#cc4 = fourcc(*'XVID') #works in 15.04,14.04 plays wherever
#fourcc = fourcc(*'FFV1') #works in 15.04 and 14.04, use VLC or FFPLAY  to playback

#** maybe works somewhat
#fourcc = fourcc(*'IYUV') # works 14.04, not work 15.04
#fourcc = fourcc(*'THEO'); ext='.ogv' #must name file .ogv, NOT .avi\  -- somewhat broken, per messages in ffplay

#*** works on 15.04 but not 14.04
#fourcc = fourcc(*'YV12') # 14.04 writes file, but file is unreadable "improper image header" -- 15.04 video works

#*** these codecs did NOT work for me on Ubuntu 14.04 or 15.04 ***
#fourcc = fourcc(*'Y41P') #silent error, no write
#fourcc = fourcc(*'YUV9') #silent error, no write -- 15.04 writes but nobody knows how to play
#fourcc = fourcc(*'DIB ') # silent error, no write
#fourcc = fourcc(*'CVID') #encoder not found
#fourcc = fourcc(*'MJ2C') #segmentation fault -- 15.04 blank video
#********************
ofn = join(gettempdir(),'test'+ext)
print('saving to ' + ofn)

hv = cv2.VideoWriter(ofn,cc4, fps=5, frameSize=(xpix,ypix), isColor=usecolor)

if not hv.isOpened():
    raise TypeError('trouble starting video file')

if usecolor:
    vdim = np.random.rand(nframe,ypix,xpix,3)
else:
    vdim = np.random.rand(nframe,ypix,xpix)

vid = (vdim*255).astype(np.uint8)
for v in vid:
    hv.write(v)

hv.release()
