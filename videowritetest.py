#!/usr/bin/python2
"""
Note: VideoWriter expects dimensions (x,y,3) and will fail otherwise,writing a tiny file perhaps
Remember, VLC has a long-standing bug where files under about 3fps don't playback

Note: the isColor parameter of VideoWriter works on Linux!
"""
import cv2
import numpy as np
from tempfile import gettempdir
from os.path import join

usecolor = False

#*** all of these codecs worked for me on Linux ***
#fourcc = cv2.cv.FOURCC(*'MJPG') #.avi
#fourcc = cv2.cv.FOURCC(*'XVID')
fourcc = cv2.cv.FOURCC(*'FFV1')
#fourcc = cv2.cv.FOURCC(*'IYUV')
#fourcc = cv2.cv.FOURCC(*'THEO') #must name file .ogv, NOT .avi
#*** these codecs did NOT work for me on Linux ***
#fourcc = cv2.cv.FOURCC(*'YV12') # writes file, but file is unreadable "improper image header"
#fourcc = cv2.cv.FOURCC(*'Y41P') #silent error, no write
# fourcc = cv2.cv.FOURCC(*'YUV9') #silent error, no write
#fourcc = cv2.cv.FOURCC(*'DIB ') # silent error, no write
#fourcc = cv2.cv.FOURCC(*'CVID') #encoder not found
#fourcc = cv2.cv.FOURCC(*'MJ2C') #segmentation fault
#********************
ofn = join(gettempdir(),'test.avi')
print('saving to ' + ofn)

hv = cv2.VideoWriter(ofn,fourcc,
                     fps=3, frameSize=(512,512), isColor=usecolor)
if not hv.isOpened():
    exit('*** trouble starting video file')

if usecolor:
    vdim = np.random.rand(100,512,512,3)
else:
    vdim = np.random.rand(100,512,512)
vid = (vdim*255).astype(np.uint8)
for v in vid:
    hv.write(v)

hv.release()
