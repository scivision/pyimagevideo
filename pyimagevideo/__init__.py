from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc as fourcc
# from cv2.cv import FOURCC as fourcc


#def videoWriter(ofn, fourcccode:str, xypix:tuple, usecolor:bool):
def videoWriter(ofn, cc4, xypix, fps, usecolor):
    """
    inputs
    ofn: string/Path output filename to write
    fourcccode: string with four character fourcc code e.g. 'FFV1'
    xypix: two-element tuple with x,y pixel count
    usecolor: bool color or bw
    """
    ncc4 = fourcc(*cc4)

    hv = VideoWriter(str(ofn), ncc4, fps=fps, frameSize=xypix, isColor=usecolor)

    if not hv or not hv.isOpened():
        raise RuntimeError('trouble starting video {}'.format(ofn))

    return hv
