""" unit test template

"""

import numpy as np
import preparation as prep

def test_dummy():
    """ unit test for dummy function """
    assert prep.dummy() == 0

def imgage():
    """creates 2d matrix to test functions"""
    xax, yax = np.meshgrid(np.linspace(0, 4 * np.pi, 256), np.linspace(0, 4 * np.pi, 256))
    matr = (0.5 * np.sin(2 * xax) * np.cos(3 * yax) + 0.3 * np.cos(5 * xax) * np.sin(2 * yax)
           + 0.2 * np.sin(3 * xax) * np.cos(4 * yax) + 0.1 * np.cos(6 * xax) * np.sin(6 * yax))
    return np.uint8((matr - np.min(matr)) / (np.max(matr) - np.min(matr)) * 255)

def test_twod_fft_mag():
    """this test makes sure that the twod_fft_mag functions properly, by testing this also makes
    sure that the length and widths of these two data sets are the same with the same assert"""
    img = imgage()
    compare = np.isclose(prep.twod_fft_mag(img),np.fft.fft2(np.array(img)), atol=1e-8)
    assert np.all(compare)

def test_twod_inv_fft():
    """this compares the inves of the fft function agenced the original unlaltered
    2d matrix this also makes sure that the length and widths of these two data
    sets are the same with the same assert"""
    img = imgage()
    compare1 = np.isclose(np.real( prep.twod_inv_fft( prep.twod_fft_mag( img ))),
                          np.array(img), atol=1e-7)
    assert np.all(compare1)

def test_twod_calc_freq():
    """This test just makes sure that what the function outputs is indeed the correct size"""
    img = imgage()
    array1, array2 = prep.twod_calc_freq(img)
    image = np.array(img)
    width, height = image.shape
    assert len(array1) == width
    assert len(array2) == height
    assert np.all(np.isclose(np.real( prep.twod_calc_freq(img)),0.0, atol=2))
