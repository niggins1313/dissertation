import cv2
import PIL
from PIL import Image
import os, sys 
 
dirs = os.listdir("/media/niggins/Seagate Backup Plus Drive/data/04Apr2016_104054/images")
count = 0
for file in dirs:
    p = "/media/niggins/Seagate Backup Plus Drive/data/04Apr2016_104054/images/"
    p+= file
    #print p
    print(count)
    if(file != 'img_00015082.png'):
        im = cv2.imread(p)
        cv2.imshow('image',im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    count+=1