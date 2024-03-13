import cv2 as cv
import numpy as np
from PIL import Image
from util import get_limits

yellow = [0,255,255] # Change it to any color!
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvimg = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lowerlimit, upperlimit = get_limits(color=yellow)

    mask = cv.inRange(hsvimg, lowerlimit, upperlimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox() # Getting Landmark of an colored object.

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        #Drawing Rectangle Shape on the landmark
        frame = cv.rectangle(frame, (x1,y1), (x2,y2), (0,100,20), thickness=3) 
        

 
    cv.imshow('Frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()