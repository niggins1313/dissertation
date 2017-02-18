import cv2
import numpy as np
import os,sys
from sklearn.ensemble import RandomForestRegressor
import csv
with open("/media/niggins/Seagate Backup Plus Drive/data/14Apr2016_093054/control.txt") as f:
    reader = csv.reader(f, delimiter="\t")
    controls = list(reader)
#with open("/media/niggins/Seagate Backup Plus Drive/data/14Apr2016_093054/control.txt") as f:
controls = np.array(controls)
print(controls.shape)
dir = os.listdir("/media/niggins/Seagate Backup Plus Drive/data/14Apr2016_093054/images")
path = "/media/niggins/Seagate Backup Plus Drive/data/14Apr2016_093054/greyimages/"
winSize = (64,64)
blockSize = (16,16)
blockStride = (8,8)
cellSize = (8,8)
nbins = 9
derivAperture = 1
winSigma = 4.
histogramNormType = 0
L2HysThreshold = 2.0000000000000001e-01
gammaCorrection = 0
nlevels = 64
hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins,derivAperture,winSigma,
                        histogramNormType,L2HysThreshold,gammaCorrection,nlevels)
#compute(img[, winStride[, padding[, locations]]]) -> descriptors
winStride = (8,8)
padding = (8,8)
locations = ((10,20),)

hist = []
count = 0
for file in dir:
    p = path + file
    hog = cv2.HOGDescriptor()
    im = cv2.imread(p)
    h = hog.compute(im,winStride,padding,locations)   
    hist.append(h)
    if(count> 10):
        break
    count+=1
nphist = np.array(hist)
print("original:", nphist.shape)
nphist = np.reshape(nphist, (12,3780))
print(nphist.shape)


