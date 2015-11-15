#!/usr/bin/env python3
"""
demonstrate RGB,BGR, etc. conversions
Michael Hirsch
"""
from tempfile import gettempdir
from os.path import join
from six.moves.urllib.request import urlretrieve
from six import PY2
from scipy.ndimage import imread
from matplotlib.pyplot import subplots,show
if PY2: FileNotFoundError=IOError

url='http://1zelda.com/tv/pics/rgb_test.jpg'
fn = 'rgb.jpg'

def loadimg(url,fn):
    fn = join(gettempdir(),fn)
    try:
        img = imread(fn)
    except FileNotFoundError:
        #download (any) RGB test image. This one is red,green, blue from top to bottom
        urlretrieve(url,fn)
        img = imread(fn)
    return img

def plotimg(rgb):
    fg,ax = subplots(1,3,figsize=(15,5))

    ax[0].imshow(rgb)
    ax[0].set_title('RGB (top to bottom)')

    bgr = rgb[...,::-1]
    ax[1].imshow(bgr)
    ax[1].set_title('BGR')

    gbr = rgb[...,[2,0,1]]
    ax[2].imshow(gbr)
    ax[2].set_title('GBR')

if __name__ == '__main__':
    img = loadimg(url,fn)
    plotimg(img)
    show()