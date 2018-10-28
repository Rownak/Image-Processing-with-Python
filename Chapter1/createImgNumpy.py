#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 17:13:17 2018

@author: afarhan
"""

from PIL import Image
from matplotlib.pylab import *

import numpy as np

def createImg():
    imgList = []

        
            
    windowList = []
    windowList.append(np.zeros((3,3), np.uint8)) # full white
    windowList.append(np.ones((3,3), np.uint8)*255) # full black
    windowList.append(np.array([[0,0,0],[50,50,50],[100,100,100]]).astype('uint8')) #1/3 black
    windowList.append(np.array([[0,0,0],[255,255,255],[255,255,255]]).astype('uint8')) #2/3 black
    print windowList[0]
    combinationWinList = []
    
    combinationWinList.append(np.random.randint(0,255,(9,9)).astype('uint8'))
    
    '''
    |0|1|0|
    |1|2|1|
    |0|1|0|
    '''
    '''
    0-1 appears 8 times
    1-2 appears 4 times
    '''
    #print combinationWinList[0]
    combinationWinList[0][0:3,0:3] = windowList[0]    
    combinationWinList[0][0:3,6:9] = windowList[0]
    combinationWinList[0][6:9,0:3] = windowList[0]
    combinationWinList[0][6:9,6:9] = windowList[0]
    
    combinationWinList[0][0:3,3:6] = windowList[1]
    combinationWinList[0][3:6,0:3] = windowList[1]
    combinationWinList[0][3:6,6:9] = windowList[1]
    combinationWinList[0][6:9,3:6] = windowList[1]
    
    combinationWinList[0][3:6,3:6] = windowList[2]
    
    
    
    #print combinationWinList
    
    for i in range(100):
        c = i%10
        r = int(i/10)
        y = np.random.randint(0,255,(18,18)).astype('uint8')
        y[r:r+9, c:c+9] = combinationWinList[0]
        imgList.append(y)
        
    '''
    print "--------------------------------------"
    print imgList[0]
    print "--------------------------------------"
    print imgList[1]
    print "--------------------------------------"
    print imgList[2]
    print "--------------------------------------"
    '''
     
    return imgList
            

#main method
from matplotlib.pylab import hist

imgList=createImg()

windowsize_r = 3
windowsize_c = 3

fout = open("intensityData.txt","w")
# Crop out the window and calculate the histogram
imgCount = 0;
for img in imgList:
    
    for r in range(0,img.shape[0], windowsize_r):
        for c in range(0,img.shape[1], windowsize_c):
            print 'R: ', r, 'C', c
            window = img[r:r+windowsize_r,c:c+windowsize_c]
            print window
            blockHist = hist(window.flatten(),bins=range(0, 257, 32))
            print blockHist[0]
            print blockHist[1]
            
            blockName = 'i'+str(imgCount)+'r'+str(r/3)+'c'+str(c/3)
            fout.write(blockName+"\t"+"\t".join(str(num) for num in blockHist[0])+"\n")
    imgCount+=1
    if(imgCount==1):
        break;
fout.close()


