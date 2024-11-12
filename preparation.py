"""
dummy preparations file 

"""

import numpy as np

def dummy():
    """ dummy functions for template file"""
    return 0

def twod_fft_mag(image):
    """this function returns the magnitudes of the frequencies
    (in complex numbers) if you dont want complex numbers, have the returned data and 
    do something simmilar to np.abs(returned data) or np.real
    Also this data is hard to interprate, if you want soemnthing a bit easier to see
    do something like np.log(np.abs(returned data) + 0.001) this makes the data more
    human readible, but once you do this this is no longer correct for the invers fft function
    This function does not cut an image to the correct size
    
    all but 2 lines of this code just makes sure the input data is functioning properly by Inverting
    the calculated fft and compairing it with the original image
    """
    image_array = np.array(image)
    fs = np.fft.fft2(image_array)
    invstimge = np.real(np.fft.ifft2(fs))
    compare = np.isclose(invstimge,image, atol=1e-6)
    alcomp = np.all(compare)
    if not alcomp:
        print("Data is not evenly spaced or data points are missing")
        return None
    return fs

def twod_inv_fft(mag):
    """this returns the original image by using the output of the twod_fft_mag function"""
    newthing = np.fft.ifft2(mag)
    return np.abs(newthing)

def twod_calc_freq(image):
    """this takes in the same data as the fft equations only gives the possible frequencies
    of the data in a matrix form, since we are dealing with a 2d image the frequencys will
    come out as a 2d matrix this function should work for a rectangle image aswell as a
    square image but I have not tested this ik a square image works
    """
    image_array = np.array(image)
    width, height = image_array.shape
    y, x = np.meshgrid(np.fft.fftfreq(width), np.fft.fftfreq(height))
    return y, x
