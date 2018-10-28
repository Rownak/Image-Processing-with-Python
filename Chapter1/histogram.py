#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:52:34 2018

@author: afarhan
"""

from PIL import Image
from matplotlib.pylab import *

pil_im_grayArray = array(Image.open('empire.jpg').convert('L'))

figure()
histArray = hist(pil_im_grayArray.flatten(),20)
show()