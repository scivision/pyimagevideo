#!/usr/bin/env python
"""
Simplest demo of using PySoundDevice to playback audio from Python
https://www.scivision.co/playing-sounds-from-numpy-arrays-in-python/

python -m pip install sounddevice

http://python-sounddevice.readthedocs.io/en/latest/#usage
"""
import sounddevice
from time import sleep
from pyimagevideo import dialtone

fs = 8000  # Hz
T = 1

x = (dialtone(fs, T) * 32768).astype('int16')  # scale to int16 for sound card

sounddevice.play(x, fs)  # releases GIL


sleep(T)  # NOTE: Since sound playback is async, allow sound playback to finish before Python exits
