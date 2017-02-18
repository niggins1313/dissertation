import PIL
import cv2
from PIL import Image
import os,sys

dir = os.listdir("/media/niggins/Seagate Backup Plus Drive/data/14Apr2016_093054/images")
dirpath = "/media/niggins/Seagate Backup Plus Drive/data/14Apr2016_093054/images/"
greydir = "/media/niggins/Seagate Backup Plus Drive/data/14Apr2016_093054/greyimages/"
count = 0
for file in dir:
    #print(file)
    path = dirpath + file
    greyp = greydir + file
    im = cv2.imread(path)
    gray_image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(greyp,gray_image)
    #cv2.imshow('image',gray_image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    basewidth = 128
    img = Image.open(greyp)
    #print(img.size)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
    #print(img.size)
    img.save(greyp) 
    #print(path)
    if(count >1000):
        break
    count +=1
print(done)