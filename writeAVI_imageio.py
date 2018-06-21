#!/usr/bin/env python
"""
Note: VideoWriter expects dimensions (x,y,3) and will fail otherwise,writing a tiny file perhaps
Remember, VLC has a long-standing bug where files under about 3fps don't playback

Note: the isColor parameter of VideoWriter works on Linux!
"""
import subprocess
import numpy as np
import tempfile
import imageio

EXE = 'ffplay'  # path to your video player
usecolor = False
nframe = 30
xpix = ypix = 256

ext = '.avi'
fps = 10

# %% generate noise signal
shape = (nframe, ypix, xpix, 3) if usecolor else (nframe, ypix, xpix)

vid = (np.random.random(shape) * 255).astype(np.uint8)
# %% write lossless AVI
with tempfile.NamedTemporaryFile(suffix=ext) as f:
    imageio.mimwrite(f.name, vid)
# %% check video
    subprocess.check_call([EXE, '-autoexit', f.name])
