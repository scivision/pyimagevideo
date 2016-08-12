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
X=Y=128; N=50
FPS=15  # keep greater than 3 to avoid VLC playback bug
WRITER = 'ffmpeg'

def testdata(x,y,N):
    # TODO: better example data to show downsides of lossy video
    return uniform(size=(N,y,x))

def setupfig(img,title=''):
    #%% boilerplate for making imshow priming (used in any program)
    assert img.ndim==2,'2-D image expected'
    fg = figure()
    ax = fg.gca()
    h = ax.imshow(img) #prime figure with first frame of data
    ax.set_title(title,color='g')
    return fg,h

def loop(fg,h,w,fn,imgs):
    assert imgs.ndim in (3,4),'assuming image stack iterating over first dimension Nframe x X x Y [x RGB]'

    with w.saving(fg, fn, DPI):
        print('writing {}'.format(fn))
        for I in imgs:
            h.set_data(I)
            draw()
            # NOTE: pause is NEEDED for more complicated plots, to avoid random crashes
            pause(0.01)
            w.grab_frame(facecolor='k')

    close(fg)


def config(h,codec):
    Writer = anim.writers[WRITER]
    return Writer(fps=FPS, codec=codec)

if __name__ == '__main__':
    imgs = testdata(X,Y,N)
#%% lossless
    fg,h = setupfig(imgs[0],'lossless')
    w = config(h,'ffv1')
    loop(fg,h,w,'lossless.avi',imgs)
#%% lossy
    fg,h = setupfig(imgs[0],'lossy')
    w = config(h,'mpeg4')
    loop(fg,h,w,'lossy.avi',imgs)
