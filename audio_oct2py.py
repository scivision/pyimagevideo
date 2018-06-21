#!/usr/bin/env python
"""
this doesn't current work with Oct2Py
"""
import numpy as np
from oct2py import Oct2Py
from pyimagevideo import dialtone

fs = 8000  # Hz

x = (dialtone(fs) * 32768).astype(np.int16)  # scale to int16 for sound card

with Oct2Py() as oc:
    #    print(oc.audiodevinfo())
    a = oc.audioplayer(x, fs)
    oc.play(a)
