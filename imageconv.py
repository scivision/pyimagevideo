#!/usr/bin/env python3
from __future__ import division,absolute_import
#
from pyimagevideo.imagemultipage import png2multipage

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='takes directory of sequential PNG plots to single multipage TIFF')
    p.add_argument('odir',help='directory with lots of PNGS')
    p.add_argument('--inext',help='read file extension',default='.png')
    p.add_argument('--outext',help='write file extension',default='.tif')
    p = p.parse_args()

    tlist = png2multipage(p.odir,p.inext,p.outext)
