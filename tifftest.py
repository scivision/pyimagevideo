from skimage.io._plugins import freeimage_plugin as freeimg
import numpy as np

x = (np.random.rand(10,512,512)*255).astype(np.uint8)

freeimg.write_multipage(x, '/tmp/junk.tif')