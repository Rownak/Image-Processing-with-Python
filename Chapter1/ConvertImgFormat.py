#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:36:45 2018

@author: afarhan
"""

from PIL import Image
import os

def get_imlist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]


path ="Images"
filelist = get_imlist(path)
for infile in filelist:
    
    outfile = os.path.splitext(infile)[0] + ".png"
    if infile != outfile:
        try:
            print outfile
            Image.open(infile).save(outfile)
        except IOError:
            print "cannot convert", infile
