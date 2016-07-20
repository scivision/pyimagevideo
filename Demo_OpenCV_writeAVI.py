#!/usr/bin/env python
"""
Note: VideoWriter expects dimensions (x,y,3) and will fail otherwise,writing a tiny file perhaps
Remember, VLC has a long-standing bug where files under about 3fps don't playback

Note: the isColor parameter of VideoWriter works on Linux!
"""
import numpy as np
from tempfile import mkstemp
from pyimagevideo import Path
#
from pyimagevideo.writeavi_opencv import videoWriter

usecolor = False
nframe=100
xpix=ypix=256

ext='.avi'
"""
all of these codecs worked for me on Ubuntu 14.04 and 16.04
'MJPG' works in 16.04, 14.04 plays wherever
'XVID' works in 16.04, 14.04 plays wherever
'FFV1' works in 16.04, 14.04, use VLC or FFPLAY  to playback

** maybe works somewhat
'IYUV' # works 14.04, not work 15.04
'THEO' ext='.ogv' #must name file .ogv, NOT .avi\  -- somewhat broken, per messages in ffplay

#*** works on 15.04 but not 14.04
'YV12' # 14.04 writes file, but file is unreadable "improper image header" -- 15.04 video works

*** these codecs did NOT work for me on Ubuntu 14.04 or 15.04 ***
'Y41P' #silent error, no write
'YUV9' #silent error, no write -- 15.04 writes but nobody knows how to play
'DIB ' # silent error, no write
'CVID' #encoder not found
'MJ2C' #segmentation fault -- 15.04 blank video
"""
#%% generate noise signal
ofn = mkstemp(ext)[1]
if usecolor:
    vdim = np.random.rand(nframe,ypix,xpix,3)
else:
    vdim = np.random.rand(nframe,ypix,xpix)

vid = (vdim*255).astype(np.uint8)
#%% write lossless AVI
hv = videoWriter(ofn,'FFV1',(xpix,ypix),usecolor)
for v in vid:
    hv.write(v)

hv.release()
