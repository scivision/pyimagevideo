"""
example
writing matplotlib movies with matlab "grabframe"-like syntax
Michael hirsch

Just four lines of code to directly write lossless AVIs from Matplotlib
"""

from matplotlib.pyplot import figure,draw,pause
import matplotlib.animation as anim
from tempfile import mkstemp
from numpy.random import uniform

fn = mkstemp(suffix='.avi')[1]

# Set up formatting for the movie files
Writer = anim.writers['ffmpeg']
writer = Writer(fps=15, codec='ffv1')
#%% random image setup
imsize = (256,256)
Nframe = 50
#%% boilerplate for making imshow priming (used in any program)
fg = figure()
ax = fg.gca()
hi = ax.imshow(uniform(size=imsize))
#%% add writer context and grabframe to typical imshow loop
with writer.saving(fg, fn,150):
    print('writing {}'.format(fn))
    for _ in range(50):
        hi.set_data(uniform(size=imsize))
        draw(),pause(0.01)
        writer.grab_frame(facecolor='k')