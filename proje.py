import cv2
import numpy as np
from threading import Thread
import time


cap = cv2.VideoCapture(0)


face_cascade = cv2.CascadeClassifier("/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/haarcascade_eye.xml")



def frame_1():


        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(gray, 1.3,5)

        for (x,y,w,h) in eyes:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255,), 1)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]


        cv2.imshow('img', img)
        cv2.waitKey(100) & 0xff



def frame_2():

        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255,), 1)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

        cv2.imshow('img2', img)
        cv2.waitKey(100) & 0xff


while True:
    frame_1()
    frame_2()


