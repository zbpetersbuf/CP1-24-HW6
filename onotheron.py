"""
np.log(np.abs(FS_shifted) + 1)

"""

import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image

def twod_fft_powerspectrum(image):
    """This function takes the function in and outputs
    the powerspectrum"""
    FS = np.fft.fft2(image.values)
    return np.log(np.abs(FS) + 0.001)

def twod_fft_mag(image):
    """this function is simalare to fft_powerspectrum only it does not cut the
    matrix imge thing, also is not realy presentable"""
    return np.fft.fft2(image.values)

def twod_inv_fft(mag):
    """this invers fft's input is the output of the fft_mag function
    do not enter in the fft_powerspectrum cause the output of this would be wrong
    ie not inv_fft(fft_powerspectrum(data)), but inv_fft(fft_mag(data))"""
    newthing = np.fft.ifft2(mag)
    return np.abs(newthing)

def twod_calc_freq(image):
    """this takes in the same data as the fft equations only gives the frequencies
    of the data, this gives out the frequencies in Hz, if you want to change it to
    days say day in the second imput, or if you want it in months say month (ie 365.25/12 days) """
    legth = image.size
    Y, X = np.meshgrid(np.fft.fftfreq(legth), np.fft.fftfreq(legth))
    return Y, X
