#!/usr/bin/env python
"""
demonstrate RGB,BGR, etc. conversions
http://1zelda.com/tv/pics/rgb_test.jpg

Michael Hirsch
"""
import imageio
from matplotlib.pyplot import subplots, show


def plotimg(rgb):
    """plot RGB, BGR, GBR"""
    fg, ax = subplots(1, 3, figsize=(15, 4))

    ax[0].imshow(rgb, origin='upper')
    ax[0].set_title('RGB')

    bgr = rgb[..., ::-1]
    ax[1].imshow(bgr, origin='upper')
    ax[1].set_title('BGR')

    gbr = rgb[..., [2, 0, 1]]
    ax[2].imshow(gbr, origin='upper')
    ax[2].set_title('GBR')

    fg.suptitle("Color order top to bottom")


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('--noshow', help='for self-test', action='store_true')
    P = p.parse_args()

    fn = 'tests/rgb.png'
    img = imageio.imread(fn)

    plotimg(img)

    if not P.noshow:
        show()
