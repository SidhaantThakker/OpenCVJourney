import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read(0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video Feed', frame)
    cv2.imshow('Greyscale Feed', gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break