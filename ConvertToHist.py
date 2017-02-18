import cv2
import pickle
import numpy as np
import os, sys

controlFile = open("/media/niggins/Seagate Backup Plus Drive/data/04Apr2016_104054/control.txt")
lines= controlFile.readlines()
dirs = os.listdir("/media/niggins/Seagate Backup Plus Drive/data/14Apr2016_093054/images/")
#image = cv2.imread("/media/niggins/Seagate Backup Plus Drive/data/04Apr2016_104054/images/img_00015082.png",0)

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
#hist = hog.compute(image,winStride,padding,locations)
hists = []
#hists.append(hist)
#hists.append(tist)


i = 0
j = 0
#controls = []
#for line in lines:
    
 #   controls.append(line.split()[1:])
  #  j = j +1
   # if (j==10):
    #    break
d = "/media/niggins/Seagate Backup Plus Drive/data/14Apr2016_093054/images/"
greydir = "/media/niggins/Seagate Backup Plus Drive/data/14Apr2016_093054/greyimages/"
front = "img_"
back = ".png"

dirs = os.listdir("/media/niggins/Seagate Backup Plus Drive/data/14Apr2016_093054/greyimages")
print(len(dirs))

for num in range(len(dirs)):
    file = front + str(num).zfill(8) + back
    im = cv2.imread(d+ file,0)
    h = hog.compute(im,winStride,padding,locations)
    hists.append(h)
    i+=1
    
    
#for file in dirs:
 #   p = "/media/niggins/Seagate Backup Plus Drive/data/14Apr2016_093054/greyimages/"
  #  p+= file
   # #print p
    #im = cv2.imread(p)
    #h = hog.compute(im,winStride,padding,locations)
  # 
  #  hists.append(h)
  #  i += 1

h = np.array(hists)

#c = np.array(controls)
print(i)
h = np.reshape(h, (i,1764))
print (h.shape)


#forest.fit(h,c)

#testImage = cv2.imread("img_00000031.png")
#test = hog.compute(testImage,winStride,padding,locations)
#test = np.reshape(test,(1,1764))
#print test.shape
#print forest.predict(test)

with open('histograms', 'wb') as f:
    pickle.dump(h, f)
