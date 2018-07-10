#!/usr/bin/env python
import subprocess
import pytest
from pathlib import Path

R = Path(__file__).parents[1]


def test_rgbbgr():
    subprocess.check_call(['python', 'RGB_BGR_GBR_conv.py', '--noshow'], cwd=R)


if __name__ == '__main__':
    pytest.main()
