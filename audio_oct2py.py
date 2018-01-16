#!/usr/bin/env python
import numpy as np
from oct2py import Oct2Py

fs = 8000 # Hz
T = 1. # second, arbitrary length of tone

# 1 kHz sine wave, 1 second long, sampled at 8 kHz
t = np.arange(0,T,1/fs)
x = 0.5 * np.sin(2*np.pi*1000*t)   # 0.5 is arbitrary to avoid clipping sound card DAC
x  = (x*32768).astype(np.int16)  # scale to int16 for sound card

with Oct2Py() as oc:
#    print(oc.audiodevinfo())
    a = oc.audioplayer(x,fs)
    oc.play(a)
