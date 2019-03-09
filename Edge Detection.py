import cv2
import numpy as np
import argparse
#from transform import four_point_transform
import matplotlib
from matplotlib.pyplot import imshow
from matplotlib import pyplot as plt



cv2.namedWindow("Mac Camera")
vc = cv2.VideoCapture(0)
#standard for macbook

while True:
    out, frame = vc.read()
    gray = cv2.cvtColor(frame, cv2.IMREAD_GRAYSCALE)
    #converts to grayscale

    kernel_size = 7
    #has to be an odd number
    #determines how grainy it will be, 5 or 7 work the best so far
    
    blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)
    #this blurs it so it makes it complete black/white and grain
    #based on the kernel size defined
    
    lowVal = 50
    highVal = 100
    #these values can be adjusted to have more or less gradient between what
    #what will be white and what will be black
    
    edges = cv2.Canny(blur_gray, lowVal, highVal)
    #this seperates the high from the low to make it show the edges

    cv2.imshow('BlackWhite', edges)
    #show the black and white version



    key = cv2.waitKey(20)
    if key == 27: # exit on ESC key
        break
    
cv2.destroyWindow("Mac Camera")
cv2.destroyWindow('BlackWhite')

#modified from https://stackoverflow.com/questions/604749/how-do-i-access-my-webcam-in-python



