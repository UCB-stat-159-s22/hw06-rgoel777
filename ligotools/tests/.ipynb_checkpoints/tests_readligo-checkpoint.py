import numpy as np
from scipy import signal
from scipy.interpolate import interp1d
from scipy.signal import butter, filtfilt, iirdesign, zpk2tf, freqz
from scipy.io import wavfile
import h5py
import json
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import os
import os.path

# LIGO-specific readligo.py 
from ligotools import readligo as rl
from ligotools import utils as ut

hdf1 = rl.read_hdf5('data/L-L1_LOSC_4_V2-1126259446-32.hdf5')
hdf2 = rl.read_hdf5('data/H-H1_LOSC_4_V2-1126259446-32.hdf5')


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
    
def utiltest1():
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata("/home/jovyan/hw/hw06-rgoel777/data/H-H1_LOSC_4_V2-1126259446-32.hdf5", 'H1')
    Pxx_H1, freqs = mlab.psd(strain_H1, Fs = 4096, NFFT = 4*4096)
    psd_H1 = interp1d(freqs, Pxx_H1)
    dt = time_H1[1] - time_H1[0]
    strain_H1_whiten = ut.whiten(strain_H1,psd_H1,dt)
    assert type(strain_H1_whiten) == np.ndarray
    assert len(strain_H1_whiten) == 131072

def utiltest2():
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata("/home/jovyan/hw/hw06-rgoel777/data/H-H1_LOSC_4_V2-1126259446-32.hdf5", 'H1')
    Pxx_H1, freqs = mlab.psd(strain_H1, Fs = 4096, NFFT = 4*4096)
    psd_H1 = interp1d(freqs, Pxx_H1)
    dt = time_H1[1] - time_H1[0]
    strain_H1_whiten = ut.whiten(strain_H1,psd_H1,dt)
    ut.write_wavfile('GW150914', 4096, strain_H1_whiten)
    wav = wavfile.read('GW150914')
    assert len(wav) == 2
    assert wav[0] == 4096
    assert type(wav[1]) == np.ndarray
    os.remove('GW150914')

def utiltest3():
    strain_L1, time_L1, chan_dict_L1 = rl.loaddata("/home/jovyan/hw/hw06-rgoel777/data/L-L1_LOSC_4_V2-1126259446-32.hdf5", 'L1')
    Pxx_L1, freqs = mlab.psd(strain_L1, Fs = 4096, NFFT = 4*4096)
    dt = time_L1[1] - time_L1[0]
    WL = lg.whiten(strain_L1, interp1d(freqs, Pxx_L1), dt)
    shift = lg.reqshift(WL, 400., 4096)
    assert strain_L1_shift.max() == 91.63543337076183
    assert strain_L1_shift.min() == -88.35025813837271
    assert len(strain_L1_shift) == 131072

def utiltest4():
    assert os.path.exists("/home/jovyan/hw/hw06-rgoel777/figures/GW150914_H1_matchfreq.png") == True
    assert os.path.exists("/home/jovyan/hw/hw06-rgoel777/figures/GW150914_H1_matchtime.png") == True

    