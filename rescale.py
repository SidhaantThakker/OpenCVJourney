import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def change_res(frame, width, height):
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

def rescale_frame(frame, percent):
    width = int(frame.shape[1]*percent/100)
    height = int(frame.shape[0]*percent/100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

while True:
    ret, frame = cap.read()
    downscale = rescale_frame(frame, 50)
    upscale = rescale_frame(frame, 150)
    reschange = change_res(frame, 600, 400)
    cv2.imshow('Original Frame', frame)
    cv2.imshow('50% Frame', downscale)
    cv2.imshow('150% Frame', upscale)
    cv2.imshow('600x400 Frame', reschange)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()