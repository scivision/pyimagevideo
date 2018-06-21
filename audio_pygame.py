#!/usr/bin/env python
"""
Simplest demo of using PyGame to playback audio from Python
https://www.scivision.co/playing-sounds-from-numpy-arrays-in-python/
"""
import pygame
from time import sleep
from pyimagevideo import dialtone

fs = 8000  # Hz

x = (dialtone(fs) * 32768).astype('int16')  # scale to int16 for sound card


pygame.mixer.pre_init(fs, size=-16, channels=1)
pygame.mixer.init()
sound = pygame.sndarray.make_sound(x)

sound.play()

sleep(0.01)  # NOTE: Since sound playback is async, allow sound playback to start before Python exits
