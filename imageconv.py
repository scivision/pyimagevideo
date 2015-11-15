#!/usr/bin/env python3
from __future__ import division,absolute_import
import logging
from pathlib2 import Path
import re
from scipy.ndimage import imread # much better than PIL
from scipy.misc import imresize #ditto
from numpy import empty
from warnings import warn

#from visvis.vvmovie.images2gif import writeGif #garbage doesn't work correctly, bad GIFs
#note tifffile is 20x faster than freeimage
import tifffile

def png2multipage(odir,inext,outext='.tif',descr='',delete=False):
    odir = Path(odir).expanduser()
    assert odir.is_dir()

    # only files matching regex
    pat ='(.*)_t\d+\\'+inext+'$'
    logging.info('using regex {}'.format(pat))
    tlist = filterPick(odir.iterdir(),pat)
    logging.info('{} file types found in {}'.format(len(tlist),odir))
#%% convert these sets of images to multipage image
    for t in tlist:
        gfn = odir/(t+outext) #final multipage filename for this image type
        flist = sorted(odir.glob(Path(t).name+'*'+inext))

        logging.debug('globbed files {} to put into {}'.format(flist,gfn))
        if not flist:
            return ValueError('unexpected problem globbing, found no files')

        im0 = imread(str(flist[0]),mode='RGB') #priming read

        images = empty((len(flist),im0.shape[0],im0.shape[1],im0.shape[2]),dtype=im0.dtype)
        for i,f in enumerate(flist):
            try:
                images[i,...]=imresize(imread(str(f),mode='RGB'),im0.shape)#they are all of slightly different shape
            except OSError as e:
                warn('skipping {} due to {}'.format(f,e))
                continue
            if delete:
                f.unlink()
        #writeGif(gfn,images,duration=0.1,repeat=True)
        tifffile.imsave(str(gfn),images,compress=6,description=descr)

def filterPick(lines, regex):
    """
    http://stackoverflow.com/questions/2436607/how-to-use-re-match-objects-in-a-list-comprehension
    """
    matches = map(re.compile(regex).match, (str(l) for l in lines))
    return set([m.group(1) for m in matches if m])

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='takes directory of sequential PNG plots and makes an animated GIF')
    p.add_argument('odir',help='directory with lots of PNGS')
    p.add_argument('--inext',help='read file extension',default='.png')
    p.add_argument('--outext',help='write file extension',default='.tif')
    p.add_argument('-v','--verbose',help='debug msg',action='count',default=0)
    p = p.parse_args()

    tlist = png2multipage(p.odir,p.inext,p.outext)
