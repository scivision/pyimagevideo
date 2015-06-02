#!/usr/bin/env python3
from os.path import expanduser, join
from os import listdir, remove
import re
from glob import glob
from scipy.ndimage import imread # much better than PIL
from scipy.misc import imresize #ditto
from numpy import empty
from warnings import warn

#from visvis.vvmovie.images2gif import writeGif #garbage doesn't work correctly, bad GIFs

try: #note tifffile is 20x faster than freeimage
    from image_write_multipage import write_multipage_tiff
except ImportError:
    from .image_write_multipage import write_multipage_tiff

def png2multipage(odir,inext,outext='.tif',descr='',delete=False,verbose=0):
    odir = expanduser(odir)
    olist = listdir(odir)

    # let's get the "first" file for each filetype
    pat ='.*_t0+\\'+inext+'$'
    if verbose>0: print('using regex {}'.format(pat))
    tlist = filterPick(olist,pat)
    #extract the prefixes for these files
    pref = [f.split('_t')[0] for f in tlist]
    if verbose>0: print('{} files found in {}'.format(len(pref),odir))
#%% convert these sets of images to multipage image
    for p in pref:
        gfn = join(odir,p+outext)
        flist = glob(join(odir,p+'*'+inext))
        flist.sort() #in-place method

        if verbose>0:
            print('globbed files {} to put into {}'.format(flist,gfn))
        if not flist:
            warn('unexpected problem globbing, found no files')
            return
        try:
            im0 = imread(flist[0],mode='RGB')
        except OSError as e:
            warn('could not read first image {}, returning.  {}'.format(flist[0],e))
            return
        images = empty((len(flist),im0.shape[0],im0.shape[1],im0.shape[2]),dtype=im0.dtype)
        for i,f in enumerate(flist):
            try:
                images[i,...]=imresize(imread(f,mode='RGB'),im0.shape)#they are all of slightly different shape
            except OSError as e:
                warn('skipping {} due to {}'.format(f,e))
                continue
            if delete:
                remove(f)
        #writeGif(gfn,images,duration=0.1,repeat=True)
        write_multipage_tiff(images,gfn,descr=descr,verbose=verbose)



def filterPick(lines, regex):
    """
    http://stackoverflow.com/questions/2436607/how-to-use-re-match-objects-in-a-list-comprehension
    """
    matches = map(re.compile(regex).match, lines)
    return [m.group(0) for m in matches if m]

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='takes directory of sequential PNG plots and makes an animated GIF')
    p.add_argument('odir',help='directory with lots of PNGS')
    p.add_argument('--inext',help='read file extension',default='.png')
    p.add_argument('--outext',help='write file extension',default='.tif')
    p.add_argument('-v','--verbose',help='debug msg',action='count',default=0)
    p = p.parse_args()

    tlist = png2multipage(p.odir,p.inext,p.outext,'',False,p.verbose)
