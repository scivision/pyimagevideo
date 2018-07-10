#!/usr/bin/env python
import pytest
from pathlib import Path
try:
    import cv2
except ImportError:
    cv2 = None

R = Path(__file__).parents[1]


@pytest.mark.skipif(cv2 is None, reason='OpenCV not installed')
def test_cv2codec_read():
    fn = R / 'tests/star_collapse_out.avi'
    vid = cv2.VideoCapture(str(fn))

    ret, img = vid.read()  # a 3-D Numpy array, last axis is BGR: blue,green,red
    vid.release()

    assert ret, 'could not open video'
    assert img.shape == (480, 720, 3), 'video not decoded properly'

    cv2.imshow(fn.name, img)
    cv2.waitKey(delay=1000)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    pytest.main()
