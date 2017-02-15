import logging
from pathlib import Path
import re
from scipy.ndimage import imread # much better than PIL
from scipy.misc import imresize #ditto
from numpy import empty

#from visvis.vvmovie.images2gif import writeGif #garbage doesn't work correctly, bad GIFs
#note tifffile is 20x faster than freeimage
import tifffile


def png2multipage(odir,inext,outext='.tif',descr='',delete=False):
    odir = Path(odir).expanduser()
    assert odir.is_dir()

    # only files matching regex
    pat ='(.*)_t\d+\\'+inext+'$'
    logging.info(f'using regex {pat}')
    tlist = filterPick(odir.iterdir(),pat)
    logging.info(f'{len(tlist)} file types found in {odir}')
#%% convert these sets of images to multipage image
    for t in tlist:
        gfn = odir/(t+outext) #final multipage filename for this image type
        flist = sorted(odir.glob(Path(t).name+'*'+inext))

        logging.debug(f'globbed files {flist} to put into {gfn}')
        if not flist:
            return ValueError('unexpected problem globbing, found no files')

        im0 = imread(str(flist[0]),mode='RGB') #priming read

        images = empty((len(flist),im0.shape[0],im0.shape[1],im0.shape[2]),dtype=im0.dtype)
        for i,f in enumerate(flist):
            try:
                images[i,...]=imresize(imread(str(f),mode='RGB'),im0.shape)#they are all of slightly different shape
            except OSError as e:
                logging.warning(f'skipping {f} due to {e}')
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
