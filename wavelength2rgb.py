#!/usr/bin/env python
from __future__ import division

def wavelength_to_rgb(wavelength, gamma=0.8):

    '''
    noah.org
    http://www.noah.org/wiki/Wavelength_to_RGB_in_Python

    This converts a given wavelength into an approximate RGB value.
    The given wavelength is in nanometers.
    The range of wavelength is 380 nm through 750 nm.

    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    '''

    wavelength = float(wavelength)
    if 440. >= wavelength >= 380.:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.
        B = (1. * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.
        G = 1.
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.
        B = 0.
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.
        B = 0.
    else:
        R = 0.
        G = 0.
        B = 0.

    R = int(R*255)
    G = int(G*255)
    B = int(B*255)

    assert 255>=R>=0 and 255>=G>=0 and 255>=B>=0

    return R,G,B

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('wavelength_nm',help='wavelength in nm',type=float)
    p.add_argument('--gamma',type=float,default=0.8)
    p = p.parse_args()

    R,G,B = wavelength_to_rgb(p.wavelength_nm,p.gamma)

    print(R)
    print(G)
    print(B)
