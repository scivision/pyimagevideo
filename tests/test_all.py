#!/usr/bin/env python
import unittest
import subprocess
from pathlib import Path
#
import matplotlib
matplotlib.use('agg')
#
import pyimagevideo

R = Path(__file__).parents[1]

class BasicTests(unittest.TestCase):

    def test_rgbbgr(self):
        subprocess.check_call(['python','RGB_BGR_GBR_conv.py','--noshow'], cwd=R)

    def test_tiff_multipage_rw(self):
        subprocess.check_call(['python','Image_write_multipage.py'], cwd=R)

if __name__ == '__main__':
    subprocess.check_call(['python','gentestimgs.py'], cwd=R/'tests')
    unittest.main()