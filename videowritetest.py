"""
Not working 2015-Feb-13
need to custom compile opencv with ffmpeg?
"""
import cv2
import numpy as np

fourcc = cv2.cv.FOURCC('M','J','P','G')
hv = cv2.VideoWriter('/tmp/test.avi',fourcc,fps=10.0,frameSize=(512,512))#,isColor=0)
print(hv.isOpened())
x = np.random.rand(512,512)
hv.write(x)
hv.write(x)

hv.release()