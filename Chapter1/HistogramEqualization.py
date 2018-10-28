#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 15:18:48 2018

@author: rownak
"""

import numpy as np
import cv2
from PIL import Image
from matplotlib import pylab as plt

def histeq(im,nbr_bins=256):
    """ Histogram equalization of a grayscale image. """
    # get image histogram
    imhist,bins = np.histogram(im.flatten(),nbr_bins,normed=True)
    cdf = imhist.cumsum() # cumulative distribution function
    cdf = 255 * cdf / cdf[-1] # normalize
    # use linear interpolation of cdf to find new pixel values
    im2 = np.interp(im.flatten(),bins[:-1],cdf)
    return im2.reshape(im.shape), cdf


path = "images/empire.jpg"

im = cv2.imread(path,1)
cv2.imshow('HistEqu.jpg', im)
cv2.waitKey(1)

'''
#eq_im, cdf = histeq(img,256)
nbr_bins=20
imhist,bins = np.histogram(im.flatten(),nbr_bins,normed=True)
cdf = imhist.cumsum() # cumulative distribution function
cdf = 255 * cdf / cdf[-1] # normalize
# use linear interpolation of cdf to find new pixel values
im2 = np.interp(im.flatten(),bins[:-1],cdf)
eq_im=im2.reshape(im.shape).astype(np.uint8)

cv2.imshow('Hist Equ', np.hstack((im,eq_im)))
'''