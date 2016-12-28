#!/usr/bin/env python
"""
compare with demo_findpeaks.m
"""
from numpy import array
from scipy.signal import savgol_filter,argrelmax
from matplotlib.pyplot import figure,show

noisy = array([1,3,5,2,1,5,5.01,0,2,4,6,0,7,1,0])
pkind = array(argrelmax(noisy,order=1))

ax= figure().gca()
ax.plot(noisy,color='k')
ax.plot(pkind,noisy[pkind],linestyle='none',marker='*',markersize=10,color='r')
ax.set_xlabel('index (zero-based)')
ax.set_ylabel('value')

show()
