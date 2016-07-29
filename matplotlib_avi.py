#!/usr/bin/env python
"""
example writing matplotlib movies with matlab "grabframe"-like syntax

Just four lines of code to directly write lossless AVIs from Matplotlib
lines 22-24,29 are all that's needed.
"""
import matplotlib
matplotlib.use('agg') #invisible while plotting, but faster and more robust
from matplotlib.pyplot import figure,draw,pause
import matplotlib.animation as anim
from tempfile import mkstemp
from numpy.random import uniform

DPI=100

fn = mkstemp('.avi','lossless')[1]

#%% random image setup
imsize = (128,128)
Nframe = 20
#%% boilerplate for making imshow priming (used in any program)
fg = figure()
ax = fg.gca()
hi = ax.imshow(uniform(size=imsize))
#%% add writer context and grabframe to typical imshow loop
#Writer = anim.writers['mencoder']
Writer = anim.writers['ffmpeg']
writer = Writer(fps=15, codec='ffv1')
with writer.saving(fg, fn, DPI):
    print('writing {}'.format(fn))
    for _ in range(50):
        hi.set_data(uniform(size=imsize))
        draw(),pause(0.01)
        writer.grab_frame(facecolor='k')
