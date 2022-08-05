import cv2 as cv
from cv2 import FONT_HERSHEY_SIMPLEX
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

cv.imshow('Blank', blank)


# blank[:]= 0,255,0

# cv.imshow('Green', blank)

# blank[120:121, 0:500]= 0,0,255
# cv.imshow('Red', blank)

# cv.rectangle
# cv.circle
# cv.line 

#write text
cv.putText(blank,'Crazy', (100,150), FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 5)
cv.imshow('Text', blank)





cv.waitKey(0)
