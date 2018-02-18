#!/usr/bin/env python
"""uses imagemagick on the command line to generate a series of test images. 
Could have used shell script, but this is more cross-platform, without need to both using Wand.
"""
import subprocess

for i in range(10):
    cmd = ['convert','-pointsize','36',f'label:{i}',f'{i}.png']
    subprocess.run(cmd, timeout=1)
