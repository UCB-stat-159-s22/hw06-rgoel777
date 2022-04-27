import numpy as np
from scipy import signal
from scipy.interpolate import interp1d
from scipy.signal import butter, filtfilt, iirdesign, zpk2tf, freqz
import h5py
import json

# the IPython magic below must be commented out in the .py file, since it doesn't work there.
%matplotlib inline
%config InlineBackend.figure_format = 'retina'
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

# LIGO-specific readligo.py 
from ligotools import readligo as rl

hdf1 = lg.read_hdf5('data/L-L1_LOSC_4_V2-1126259446-32.hdf5')
hdf2 = lg.read_hdf5('data/H-H1_LOSC_4_V2-1126259446-32.hdf5')


def ligotest1():
    assert len(hdf1) == 7
    assert type(hdf1) == tuple
    assert type(hdf1[0]) == numpy.ndarray
    assert type(hdf1[6]) == list

def ligotest2():
    assert len(hdf2) == 7
    assert type(hdf2) == tuple
    assert type(hdf2[3]) == numpy.ndarray
    assert type(hdf2[4]) == list

def ligotest3():
    assert hdf1[0].shape == (131072,)
    assert hdf1[1].shape == ()
    assert hdf1[2].shape == ()
    assert hdf1[3].shape == (32,)
    assert hdf1[5].shape == (32,)

def ligotest4():
    assert hdf2[0].shape == (131072,)
    assert hdf2[1].shape == ()
    assert hdf2[2].shape == ()
    assert hdf2[3].shape == (32,)
    assert hdf2[5].shape == (32,)