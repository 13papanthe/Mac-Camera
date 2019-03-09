import cv2
import sys
import numpy as np
import matplotlib
from matplotlib.pyplot import imshow
from matplotlib import pyplot as plt
import logging as log
import datetime as dt

#define all the xml files that you want to call out. make sure to download them
#to wherever your saving the python file.

cascades = [
#	{ 'file':'haarcascade_eye.xml','label':'Eye' },
	{ 'file':'haarcascade_eye_tree_eyeglasses.xml','label':'Eye' },
#	{ 'file':'haarcascade_frontalcatface.xml','label':'frontalcatface' },
#	{ 'file':'haarcascade_frontalcatface_extended.xml','label':'frontalcatface_extended' },
#	{ 'file':'haarcascade_frontalface_alt.xml','label':'Front Face' },
#	{ 'file':'haarcascade_frontalface_alt2.xml','label':'frontalface_alt2' },
#	{ 'file':'haarcascade_frontalface_alt_tree.xml','label':'frontalface_alt_tree' },
	{ 'file':'haarcascade_frontalface_default.xml','label':'Face' },
#	{ 'file':'haarcascade_fullbody.xml','label':'fullbody' },
#	{ 'file':'haarcascade_lefteye_2splits.xml','label':'lefteye_2splits' },
#	{ 'file':'haarcascade_licence_plate_rus_16stages.xml','label':'licence_plate_rus_16stages' },
#	{ 'file':'haarcascade_lowerbody.xml','label':'lowerbody' },
#	{ 'file':'haarcascade_profileface.xml','label':'profileface' },
#	{ 'file':'haarcascade_righteye_2splits.xml','label':'righteye' },
#	{ 'file':'haarcascade_russian_plate_number.xml','label':'russian_plate_number' },
#	{ 'file':'haarcascade_smile.xml','label':'smile' },
#	{ 'file':'haarcascade_upperbody.xml','label':'upperbody' },
	]
#hashtag all the ones you dont want to detect in the camera.

for c in cascades:
    c['cascade'] = cv2.CascadeClassifier(c['file'])
log.basicConfig(filename='webcam.log',level=log.INFO)
#calls out all the cascades you want to filter from above.

cv2.namedWindow("Mac Camera") #what the window will be named
vc = cv2.VideoCapture(0) #sets value to call this out

for c in cascades:
    c['anterior'] = 0
#calling all the 0 ones out

#if vc.isOpened(): #pauses to make sure the frame can be read - redundant

while True:
    #keep running easier
    
    out, frame = vc.read() #output is reading the video capture as defined above
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #This converts to grayscale


# Draw a rectangle around the faces
#refrence https://github.com/furetosan/webcammer
#this part is not my code!!!
    for c in cascades:
       
        c['detects'] = c['cascade'].detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

    for c in cascades:
        if len(c['detects']) > 0:
            for i in c['detects']:
                x, y, w, h = i
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, c['label'], (x,y), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255))

        if c['anterior'] != len(c['detects']):
            c['anterior'] = len(c['detects'])
            log.info(c['label']+" detects: "+str(len(c['detects']))+" at "+str(dt.datetime.now()))




#while outputting video:
    cv2.imshow("Mac Camera", frame)
    out, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC key
        break

    
vc.release()
#releases the capture
cv2.destroyWindow("Mac Camera")
#exits out of the window

#modified from https://stackoverflow.com/questions/604749/how-do-i-access-my-webcam-in-python



