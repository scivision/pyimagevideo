#!/usr/bin/env python
"""
Note: VideoWriter expects dimensions (x,y,3) and will fail otherwise,writing a tiny file perhaps
Remember, VLC has a long-standing bug where files under about 3fps don't playback

Note: the isColor parameter of VideoWriter works on Linux!
"""
import subprocess
import numpy as np
import tempfile
#
from pyimagevideo import VideoWriter

EXE = 'ffplay'  # path to your video player
usecolor = False
nframe = 30
xpix = ypix = 256

ext = '.avi'
CC4 = 'FMP4'
fps = 10
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
# %% generate noise signal
shape = (nframe, ypix, xpix, 3) if usecolor else (nframe, ypix, xpix)

vid = (np.random.random(shape) * 255).astype(np.uint8)
# %% write lossless AVI
with tempfile.NamedTemporaryFile(suffix=ext) as f:
    with VideoWriter(f.name, CC4, (xpix, ypix), fps, usecolor) as hv:
        for v in vid:
            hv.write(v)

    subprocess.check_call([EXE, '-autoexit', f.name])
