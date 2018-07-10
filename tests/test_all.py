#!/usr/bin/env python
import tempfile
import numpy as np
import pytest
from pathlib import Path
import imageio
#
import pyimagevideo as piv
R = Path(__file__).parents[1]


def test_tiff_multipage_rw():
    with tempfile.TemporaryDirectory() as d:
        d = Path(d).expanduser()

        piv.genimgseries(d)

        ofn = d / 'mp.tif'
        piv.png2tiff(ofn, '[0-9].png')

        y = imageio.mimread(ofn)

    assert len(y) == 10


def test_wavelength2rgb():
    np.testing.assert_allclose(piv.wavelength2rgb(720), (146, 0, 0))


if __name__ == '__main__':
    pytest.main()
