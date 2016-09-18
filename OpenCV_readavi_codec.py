#!/usr/bin/env python
"""
scans a directory for all videos and plays them, helping show which codecs you might be having a problem with
"""
from pathlib import Path
import cv2
import logging
import subprocess

path = '~/Videos'
pat = '*'
#%%
print('OpenCV {} loaded from {}'.format(cv2.__version__,cv2.__file__))

path = Path(path).expanduser()
flist = sorted(path.glob(pat))

failed = []
passed = []
for fn in flist:
    if not fn.is_file():
        continue
    
    try:
        ret = subprocess.check_output(['ffprobe','-show_streams',str(fn)],stderr=subprocess.DEVNULL).decode('utf8').split('\n')
        ind = [i for i, elem in enumerate(ret) if 'codec_name' in elem]
        codec = ret[ind[0]].split('=')[1]
    except (IndexError,SubprocessError):
        codec = str(fn)
#%%
    v = cv2.VideoCapture(str(fn))
    if not v.isOpened():
        logging.error('unable to read {}'.format(fn))
        failed.append(codec)
        continue
    """
    NOTE: will still "pass" even if video is scrambled or blank
    """
    passed.append(codec) 
    while True:
        ret,frame = v.read()
        if not ret:
            break
    
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow(str(fn),gray)
        cv2.waitKey(10)
        

    v.release()
    cv2.destroyWindow(str(fn))
#%%
if passed:
    print('passing codecs:')
    print('\n'.join(passed))
    
if failed:
    print('failed codecs:')
    print('\n'.join(failed))