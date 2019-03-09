import cv2
import numpy as np
import matplotlib
from matplotlib.pyplot import imshow
from matplotlib import pyplot as plt



cv2.namedWindow("Mac Camera")
vc = cv2.VideoCapture(0)

if vc.isOpened(): #pauses to make sure the frame can be read
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("Mac Camera", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC key
        break
cv2.destroyWindow("Mac Camera")

#modified from https://stackoverflow.com/questions/604749/how-do-i-access-my-webcam-in-python



