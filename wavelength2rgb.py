#!/usr/bin/env python
from pyimagevideo import wavelength2rgb

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('wavelength_nm',help='wavelength in nm',type=float)
    p.add_argument('--gamma',type=float,default=0.8)
    p = p.parse_args()

    R,G,B = wavelength2rgb(p.wavelength_nm,p.gamma)

    print(R)
    print(G)
    print(B)
