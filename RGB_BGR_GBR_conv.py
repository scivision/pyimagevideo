#!/usr/bin/env python
"""
demonstrate RGB,BGR, etc. conversions
http://1zelda.com/tv/pics/rgb_test.jpg

Michael Hirsch
"""
from argparse import ArgumentParser
import imageio
import numpy as np
try:
    from matplotlib.pyplot import figure, show
except (ImportError, RuntimeError):
    figure = show = None


def plotimg(rgb: np.ndarray):
    """plot RGB, BGR, GBR"""
    if figure is None:
        return

    fg = figure(figsize=(15, 4))
    ax = fg.subplots(1, 3)

    ax[0].imshow(rgb, origin='upper')
    ax[0].set_title('RGB')

    bgr = rgb[..., ::-1]
    ax[1].imshow(bgr, origin='upper')
    ax[1].set_title('BGR')

    gbr = rgb[..., [2, 0, 1]]
    ax[2].imshow(gbr, origin='upper')
    ax[2].set_title('GBR')

    fg.suptitle("Color order top to bottom")


def main():
    p = ArgumentParser()
    p.add_argument('--noshow', help='for self-test', action='store_true')
    P = p.parse_args()

    fn = 'tests/rgb.png'
    img = imageio.imread(fn)

    plotimg(img)

    if show is not None and not P.noshow:
        show()


if __name__ == '__main__':
    main()
