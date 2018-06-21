try:
    import cv2
except ImportError:
    cv2 = None

from contextlib import contextmanager
import numpy as np
from matplotlib.pyplot import figure, draw, close
from pathlib import Path
import imageio
from skimage.transform import resize
from typing import List, Tuple, Union


def wavelength2rgb(wavelength: float, gamma: float=0.8) -> Tuple[float, float, float]:
    '''
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

    R = int(R * 255)
    G = int(G * 255)
    B = int(B * 255)

    assert 255 >= R >= 0 and 255 >= G >= 0 and 255 >= B >= 0

    return R, G, B


def tone(fs: int=8000, T: float=1, f0: float=1000) -> np.ndarray:
    """
    generate f0 Hz sinusoid for T seconds at fs S/s.
    """
    return np.sin(2 * np.pi * f0 * np.arange(0, T, 1 / fs))


def dialtone(fs: int=8000, T: float=1):
    """
    generate North American dial tone
    https://en.wikipedia.org/wiki/Precise_Tone_Plan
    """
    return 0.5 * (tone(fs, T, 440) + tone(fs, T, 350))


def genimgseries(odir: Path) -> List[Path]:
    odir = Path(odir).expanduser()

    fg = figure(1, figsize=(0.5, 0.5))
    # fg.set_visible(False)
    ax = fg.gca()

    flist = []
    for i in range(10):
        ax.clear()
        ax.axis('off')

        ax.text(0, 0, i, fontsize=36)

        draw()

        fn = odir / f'{i}.png'
        flist.append(fn)

        fg.savefig(fn, bbox_inches='tight', pad_inches=0)

    close(fg)

    return flist


def png2tiff(ofn: Path, pat: str, indir: Path=None):
    """
    convert series of PNG, which may not be exactly the same shape,
    to a multipage TIFF (in the same directory)

    alternatives: use ImageMagick from command line, or Wand.
    however, since the files are grouped in a specific weird way, the histfeas program
    worked best to have this perhaps ImageMagick duplicative functionality in
    Python/imageio/skimage.
    """
    ofn = Path(ofn).expanduser()
    indir = ofn.parent if indir is None else Path(indir).expanduser()
# %% convert these sets of images to multipage image
    flist = sorted(indir.glob(pat))  # yes, sorted()
    if not flist:
        raise FileNotFoundError('found no files with {pat} in {ofn}')

    im0 = imageio.imread(flist[0])  # priming read
    images = np.empty((len(flist), *im0.shape), dtype=im0.dtype)
    for i, f in enumerate(flist):
        im = imageio.imread(f)
        images[i, ...] = resize(im, im0.shape, mode='edge')  # they are all of slightly different shape

    imageio.mimwrite(ofn, images)


@contextmanager
def VideoWriter(ofn: Union[str, Path], cc4: str, xypix: tuple, fps: float, usecolor: bool):
    """
    inputs
    ofn: string/Path output filename to write
    fourcccode: string with four character fourcc code e.g. 'FFV1'
    xypix: two-element tuple with x,y pixel count
    usecolor: bool color or bw
    """
    if cv2 is None:
        raise ImportError('OpenCV was not installed or loaded')

    ncc4 = cv2.VideoWriter_fourcc(*cc4)

    hv = cv2.VideoWriter(str(ofn), ncc4, fps=fps, frameSize=xypix, isColor=usecolor)

    if not hv or not hv.isOpened():
        raise RuntimeError(f'trouble starting video {ofn}')

    yield hv

    hv.release()
