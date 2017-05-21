#!/usr/bin/env python
"""
Simplest demo of using PyAudio to playback audio from Python
https://www.scivision.co/playing-sounds-from-numpy-arrays-in-python/
"""
import numpy as np
import pyaudio

fs = 8000 # Hz
T = 1. # second, arbitrary length of tone

# 1 kHz sine wave, 1 second long, sampled at 8 kHz
t = np.arange(0,T,1/fs)
x = 0.5 * np.sin(2*np.pi*1000*t)   # 0.5 is arbitrary to avoid clipping sound card DAC
x  = (x*32768).astype(np.int16)  # scale to int16 for sound card

# Sorry, PyAudio doesn't seem to have context manager
P = pyaudio.PyAudio()

stream = P.open(rate=fs, format=pyaudio.paInt16, channels=1, output=True)
stream.write(x.tobytes())

stream.close() # this blocks until sound finishes playing

P.terminate()
