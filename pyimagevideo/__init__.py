from __future__ import print_function
from sys import stderr
try:
    import cv2
except ImportError:
    cv2=None

def videoWriter(ofn, cc4:str, xypix, fps, usecolor:bool):
    """
    inputs
    ofn: string/Path output filename to write
    fourcccode: string with four character fourcc code e.g. 'FFV1'
    xypix: two-element tuple with x,y pixel count
    usecolor: bool color or bw
    """
    if cv2 is None:
        raise ImportError('OpenCV was not installed or loaded')

    ncc4 = cv2.VideoWriter_fourcc(*cc4)

    hv = cv2.VideoWriter(str(ofn), ncc4, fps=fps, frameSize=xypix, isColor=usecolor)

    if not hv or not hv.isOpened():
        raise RuntimeError('trouble starting video {}'.format(ofn))

    return hv
