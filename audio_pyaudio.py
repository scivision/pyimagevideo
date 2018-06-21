#!/usr/bin/env python
"""
Simplest demo of using PyAudio to playback audio from Python
https://www.scivision.co/playing-sounds-from-numpy-arrays-in-python/

requires libportaudio-dev

I don't use PortAudio as it conflicts with WINE.
"""
import numpy as np
import pyaudio
#
from pyimagevideo import tone

fs = 8000

x = (tone(fs) * 0.99 * 32768).astype(np.int16)  # scale to int16 for sound card, 0.99 to not clip

# Sorry, PyAudio doesn't seem to have context manager
P = pyaudio.PyAudio()

stream = P.open(rate=fs, format=pyaudio.paInt16, channels=1, output=True)
stream.write(x.tobytes())

stream.close()  # this blocks until sound finishes playing

P.terminate()
