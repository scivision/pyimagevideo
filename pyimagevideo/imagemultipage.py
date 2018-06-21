"""
These functions are for https://github.com/scivision/histfeas output plot collection
"""
import logging
from pathlib import Path
import re
from typing import Generator, List, Union
#
from . import png2tiff
# from visvis.vvmovie.images2gif import writeGif #garbage doesn't work correctly, bad GIFs
# imageio/tifffile is 20x faster than freeimage


def hist2tif(odir: Path, inext: str):
    odir = Path(odir).expanduser()
    pat = '(.*)_t\d+\\' + inext + '$'
    logging.info(f'using regex {pat}')
    tlist = filterPick(odir.iterdir(), pat)
    logging.info(f'{len(tlist)} file types found in {odir}')

    for t in tlist:
        png2tiff(odir / (t + '.tif'), pat)


def filterPick(lines: Union[Generator, List[str]], regex: str) -> set:
    """
    http://stackoverflow.com/questions/2436607/how-to-use-re-match-objects-in-a-list-comprehension
    """
    matches = map(re.compile(regex).match, (str(l) for l in lines))
    return set([m.group(1) for m in matches if m])
