#!/usr/bin/env python
"""
Simplest demo of using PyGame to playback audio from Python
https://www.scivision.co/playing-sounds-from-numpy-arrays-in-python/
"""
import numpy as np
import pygame
from time import sleep

fs = 8000 # Hz
T = 1. # second, arbitrary length of tone

# 1 kHz sine wave, 1 second long, sampled at 8 kHz
t = np.arange(0,T,1/fs)
x = 0.5 * np.sin(2*np.pi*1000*t)   # 0.5 is arbitrary to avoid clipping sound card DAC
x  = (x*32768).astype(np.int16)  # scale to int16 for sound card

pygame.mixer.pre_init(fs, size=-16, channels=1)
pygame.mixer.init()
sound = pygame.sndarray.make_sound(x)

sound.play()

sleep(0.01)  # NOTE: Since sound playback is async, allow sound playback to start before Python exits