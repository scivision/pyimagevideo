#!/usr/bin/env python
"""
Demonstrates need to have OpenCV in-place operations on contiguous Numpy arrays

https://answers.opencv.org/question/219040/fastest-way-to-convert-bgr-rgb-aka-do-not-use-numpy-magic-tricks/
"""

import cv2
import numpy as np

img1 = np.zeros([200, 200, 3], np.uint8)  # Contiguous
img2 = img1[..., ::-1]  # Non-Contiguous view

print("img1 contiguous", img1.flags["C_CONTIGUOUS"])
print("img2 contiguous", img2.flags["C_CONTIGUOUS"])
print("img1 strides", img1.strides, "img2 strides", img2.strides)

cv2.rectangle(img2, (80, 80), (120, 120), (255, 255, 255), 2)
cv2.imshow("Blank instead of rectangle, due to Numpy view instead of copy", img2)

# %% img2 should instead be created as a copy
img2 = img1[..., ::-1].copy()
assert img2.flags["C_CONTIGUOUS"]

cv2.rectangle(img2, (80, 80), (120, 120), (255, 255, 255), 2)
cv2.imshow("white hollow rectangle", img2)

cv2.waitKey(delay=0)
cv2.destroyAllWindows()
