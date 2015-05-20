#!/usr/bin/env python3
from os.path import expanduser, join
from os import listdir
import re
from glob import glob
from scipy.ndimage import imread # much better than PIL
from scipy.misc import imresize #ditto
from numpy import empty

#from visvis.vvmovie.images2gif import writeGif #garbage doesn't work correctly, bad GIFs

try:
    from image_write_multipage import rwfreeimage
except ImportError:
    from .image_write_multipage import rwfreeimage

def png2multipage(odir,inext,outext='.tif'):
    odir = expanduser(odir)
    olist = listdir(odir)

    # let's get the "first" file for each filetype
    pat ='.*_t0+\\'+inext+'$'
    print('using regex {}'.format(pat))
    tlist = filterPick(olist,pat)
    #extract the prefixes for these files
    pref = [f.split('_t')[0] for f in tlist]
#%% convert these sets of images to multipage image
    for p in pref:
        gfn = join(odir,p+outext)
        flist = glob(join(odir,p+'*'+inext))
        if not flist:
            print('imageconv: unexpected problem globbing, found no files')
            return
        im0 = imread(flist[0],mode='RGB')
        images = empty((len(flist),im0.shape[0],im0.shape[1],im0.shape[2]),dtype=im0.dtype)
        for i,f in enumerate(flist):
            images[i,...]=imresize(imread(f,mode='RGB'),im0.shape)#they are all of slightly different shape

        #writeGif(gfn,images,duration=0.1,repeat=True)
        rwfreeimage(images,gfn)



def filterPick(lines, regex):
    """
    http://stackoverflow.com/questions/2436607/how-to-use-re-match-objects-in-a-list-comprehension
    """
    matches = map(re.compile(regex).match, lines)
    return [m.group(0) for m in matches if m]

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='takes directory of sequential PNG plots and makes an animated GIF')
    p.add_argument('odir',help='directory with lots of PNGS',type=str)
    p.add_argument('--ext',help='file extension',type=str,default='.png')
    p = p.parse_args()

    tlist = png2multipage(p.odir,p.ext)
