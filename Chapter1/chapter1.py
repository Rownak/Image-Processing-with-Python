#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 02:10:40 2018

@author: afarhan
"""

from PIL import Image
import cv2
import numpy as np
from pylab import *

# read Img
pil_im = Image.open('images/empire.jpg').convert('L')

# plot a line
x= [100, 100, 400, 400]
y= [200, 500, 200, 500]


cv2.imshow('im', np.array(pil_im))
cv2.waitKey(0)