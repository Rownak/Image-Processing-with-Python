#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:52:34 2018

@author: afarhan
"""

from PIL import Image
from matplotlib import pyplot as plt 
import numpy as np

pil_im_grayArray = np.array(Image.open('images/empire.jpg').convert('L'))
histArray = np.histogram(pil_im_grayArray.flatten(),20)

plt.hist(pil_im_grayArray.flatten(), 20) 
plt.title("histogram") 
plt.show()