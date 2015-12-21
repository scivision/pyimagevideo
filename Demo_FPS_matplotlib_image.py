#!/usr/bin/env python3
"""
demo of measuring FPS performance with Matplotlib and OpenCV
i.e. how fast can I update an image plot

Eample with Python 3.5:
$ python Demo_FPS_matplotlib_image.py
matplotlib 1.5.0 average FPS 16.55  over 100 frames.
OpenCV 3.0.0-dev average FPS 639.81  over 100 frames.

"""
from numpy import uint8
from numpy.random import rand
import matplotlib
from matplotlib.pyplot import figure,draw,pause,close
from time import time
try:
    import cv2
except:
    pass
#
Nfps = 100

def randomimg(xy):
    return (rand(2,xy[0],xy[1])*255).astype(uint8)

def fpsmatplotlib(dat):
    fg = figure()
    ax = fg.gca()
    h = ax.imshow(dat[0,...])
    tic = time()
    for i in range(Nfps):
        h.set_data(dat[i%2,...])
        draw(), pause(1e-6)
    close(fg)
    return Nfps/(time()-tic)

def fpsopencv(dat):
    tic = time()
    for i in range(Nfps):
        cv2.imshow('fpstest',dat[i%2,...])
        cv2.waitKey(1) #integer milliseconds, 0 makes wait forever
    cv2.destroyAllWindows()
    return Nfps/(time()-tic)

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='measure FPS for rapidly updating plot with Matplotlib vs. OpenCV')
    p.add_argument('-p','--xypixels',help='number of pixels for x and y',type=int,default=(512,512))
    p = p.parse_args()

    dat = randomimg(p.xypixels)

    fpsmat = fpsmatplotlib(dat)
    print('matplotlib {} average FPS {:.2f}  over {} frames.'.format(matplotlib.__version__,fpsmat,Nfps))

    try:
        fpscv = fpsopencv(dat)
        print('OpenCV {} average FPS {:.2f}  over {} frames.'.format(cv2.__version__,fpscv,Nfps))
    except NameError:
        pass
