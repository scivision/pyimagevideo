#!/usr/bin/env python3
"""
demonstrate RGB, BGR, etc. conversions using image from http://1zelda.com/tv/pics/rgb_test.jpg

reference:
https://www.scivision.dev/numpy-image-bgr-to-rgb/
"""
from pathlib import Path
import imageio
import matplotlib
from matplotlib.pyplot import figure, show

try:
    import cv2
except ImportError:
    cv2 = None

# %% 0. read test file
file = Path(__file__).parent / "tests/rgb.png"
rgb = imageio.imread(file)
# %% 1. show RGB, BGR, GBR in Matplotlib
print("Matplotlib version", matplotlib.__version__)
fg = figure(figsize=(15, 4))
ax = fg.subplots(1, 3, sharey=True)

ax[0].imshow(rgb, origin="upper")
ax[0].set_title("RGB")

bgr = rgb[..., ::-1]
ax[1].imshow(bgr, origin="upper")
ax[1].set_title("BGR")

gbr = rgb[..., [2, 0, 1]]
ax[2].imshow(gbr, origin="upper")
ax[2].set_title("GBR")

fg.suptitle(f"Color order top to bottom.   {file}")
fg.tight_layout()
show()

# %% 2. show RGB, BGR, GBR in OpenCV HighGUI
if cv2 is None:
    raise SystemExit("OpenCV not available.")

print("RGB C contiguous image array?", rgb.flags["C_CONTIGUOUS"])
print("BGR C contiguous image array?", bgr.flags["C_CONTIGUOUS"])

print("OpenCV version", cv2.__version__)
cv2.imshow("RGB needs BGR array", bgr)
cv2.imshow("BGR needs RGB array", rgb)

cv2.waitKey(delay=0)
cv2.destroyAllWindows()
