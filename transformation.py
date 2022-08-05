import cv2 as cv
import numpy as np

img= cv.imread('2.jpg')

cv.imshow('img', img)

#Translation

def translate(img, x, y):
    transMat= np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated= translate(img, 100, 100)
cv.imshow('Translated', translated)
# -x --> left
# -y --> up
# x --> right
# y --> down

#Rotation

cv.waitKey(0)