import cPickle
import cv2
import numpy as np

with open('randomForest', 'rb') as f:
    forest = cPickle.load(f)
    
    
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

testImage = cv2.imread("img_00000031.png")
test = hog.compute(testImage,winStride,padding,locations)
test = np.reshape(test,(1,1764))

print forest.predict(test)