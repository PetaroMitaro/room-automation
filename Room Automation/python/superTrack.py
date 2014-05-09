import cv2
from datetime import datetime
import cv2.cv as cv
import serial
from time import sleep

tolerance=80
failCount=0
direction=0
ser=serial.Serial('/dev/ttyACM0',9600)
sleep(2)
print("beginning command")
ser.write("__begin command__")
cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

def detect(img,cascade):
    rects = cascade.detectMultiScale(img,scaleFactor=4,
    minNeighbors=2,minSize=(30,30),flags = cv.CV_HAAR_SCALE_IMAGE)
    if (len(rects)==0):
        return None
    return rects[0]

def draw_rect(img,rect):
        x1=rect[0]
        y1=rect[1]
        wf=rect[2]
        hf=rect[3]
        ##print(x1)
        global direction
        h,w,d = img.shape
        if (x1+(wf/2)>w/2+tolerance):
            direction=-1
        elif (x1+(wf/2)<w/2-tolerance):
            direction=1
        else:
            direction=0
        
cam = cv2.VideoCapture(0)
ret,img = cam.read()

try:
  while ret:
      ret,img = cam.read()
      gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
      rect=detect(gray,cascade)
      if (rect!=None):
          draw_rect(img,rect)
          failCount=0
      else:
          failCount=failCount+1
          if (failCount>=6):
              ser.write("stop")
              if (failCount==6):
                  print("lost target, changing direction")
                  direction*=-1
      print(direction)
      if (direction==-1):
          print("+80")
          ser.write("motor set: +80")
      elif (direction==1):
          print("-80")
          ser.write("motor set: -80")
      else:
          print("stop")
          ser.write("stop")
      ##cv2.imshow('facedetect',img)
except KeyboardInterrupt:
  ser.write("stop")
  sleep(0.5)
  ser.write("__end command__")
  sleep(0.5)
  ser.close()

