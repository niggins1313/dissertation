
def getControls(pathToControl):
    import cv2
    import numpy as np
    import os, sys
    
    controlFile = open(pathToControl)
    
    lines = controlFile.readlines()
    controls = []
    for line in lines:
        
        controls.append(line.split()[1:])
        
    for file in imgFileNames:
        fileNum = 