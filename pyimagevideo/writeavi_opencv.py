from os.path import abspath
from cv2 import VideoWriter
try:
    from cv2.cv import FOURCC as fourcc #Windows needs from cv2.cv
except ImportError:
    from cv2 import VideoWriter_fourcc as fourcc


def videoWriter(ofn,fourcccode:str,xypix:tuple, usecolor:bool):
    """
    inputs
    ofn: string/Path output filename to write
    fourcccode: string with four character fourcc code e.g. 'FFV1'
    xypix: two-element tuple with x,y pixel count
    usecolor: bool color or bw
    """
    cc4 = fourcc(*fourcccode)

    ofn = abspath(ofn)
    print('saving to {}'.format(ofn))

    hv = VideoWriter(ofn,cc4, fps=5, frameSize=xypix, isColor=usecolor)

    if not hv or not hv.isOpened():
        raise TypeError('trouble starting video {}'.format(ofn))

    return hv