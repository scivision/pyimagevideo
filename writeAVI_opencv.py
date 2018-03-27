#!/usr/bin/env python
"""
Note: VideoWriter expects dimensions (x,y,3) and will fail otherwise,writing a tiny file perhaps
Remember, VLC has a long-standing bug where files under about 3fps don't playback

Note: the isColor parameter of VideoWriter works on Linux!
"""
import numpy as np
from tempfile import mkstemp
#
from pyimagevideo import videoWriter

usecolor = False
nframe=100
xpix=ypix=256

ext='.avi'
CC4 = 'FMP4'
fps=20
# TODO MPG4

"""
all of these codecs worked for me on Ubuntu 14.04 and 16.04
'MJPG' Motion JPEG
'XVID' MPEG-4
'FFV1' Lossless
'FMP4' MPEG-4

** maybe works somewhat
'THEO' ext='.ogv' #must name file .ogv, NOT .avi\  -- somewhat broken, per messages in ffplay

*** NOT work for me on Ubuntu 16.04 ***
'YV12'
'IYUV'
'Y41P' #silent error, no write
'YUV9' #silent error, no write -- 15.04 writes but nobody knows how to play
'DIB ' # silent error, no write
'CVID' #encoder not found
'MJ2C' #segmentation fault -- 15.04 blank video
"""
#%% generate noise signal
ofn = mkstemp(ext,'opencv_lossless')[1]

if usecolor:
    vdim = np.random.rand(nframe,ypix,xpix,3)
else:
    vdim = np.random.rand(nframe,ypix,xpix)

vid = (vdim*255).astype(np.uint8)
#%% write lossless AVI
hv = videoWriter(ofn,CC4,(xpix,ypix),fps,usecolor)
for v in vid:
    hv.write(v)

hv.release()
