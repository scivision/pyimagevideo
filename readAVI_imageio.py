#!/usr/bin/env python
"""
tests ability of an OpenCV install to read an AVI file
imageio relies on FFmpeg
"""
import imageio
from pathlib import Path
from matplotlib.pyplot import figure, draw, pause


def testreadavi(fn: Path):

    fn = Path(fn).expanduser()

    vid = imageio.mimread(fn)

# %% play video
    ax = figure().gca()
    h = ax.imshow(vid[0])
    t = ax.set_title('')

    for i, I in enumerate(vid):
        h.set_data(I)
        t.set_text(str(i))

        draw()
        pause(0.1)


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='tests OpenCV codec reading of AVI, and displays first frame of file')
    p.add_argument('avifn', help='.avi file you want to read')
    P = p.parse_args()

    testreadavi(P.avifn)
