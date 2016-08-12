#!/usr/bin/env python
"""
example writing matplotlib movies with matlab "grabframe"-like syntax

Just four lines of code to directly write lossless AVIs from Matplotlib

http://matplotlib.org/api/animation_api.html#matplotlib.animation.FFMpegWriter

codecs:
ffv1: lossless
mpeg4: lossy

"""
import matplotlib
matplotlib.use('agg') #invisible while plotting, but faster and more robust
from matplotlib.pyplot import figure,draw,pause,close
import matplotlib.animation as anim
#
from numpy.random import uniform

DPI=100
IMXY=(128,128)
FPS=15  # keep greater than 3 to avoid VLC playback bug
WRITER = 'ffmpeg'

def setupfig(shape):
    #%% boilerplate for making imshow priming (used in any program)
    assert len(shape)==2,'2-D image expected'
    fg = figure()
    ax = fg.gca()
    h = ax.imshow(uniform(size=shape))
    return fg,h

def loop(fg,h,w,fn):
    with w.saving(fg, fn, DPI):
        print('writing {}'.format(fn))
        for _ in range(50):
            h.set_data(uniform(size=IMXY))
            draw()
            # NOTE: pause is NEEDED for more complicated plots, to avoid random crashes
            pause(0.01)
            w.grab_frame(facecolor='k')

def config(h,codec):
    Writer = anim.writers[WRITER]
    return Writer(fps=FPS, codec=codec)

if __name__ == '__main__':
    fg,h = setupfig(IMXY)
#%% lossless
    w = config(h,'ffv1')
    loop(fg,h,w,'lossless.avi')
#%% lossy
    w = config(h,'mpeg4')
    loop(fg,h,w,'lossy.avi')
#%% cleanup invisible figure
    close('all')
