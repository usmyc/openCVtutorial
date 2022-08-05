import cv2 as cv
import numpy as np

img = cv.imread('1.jpeg')
cv.imshow('cat', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


# # blur
# blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# # Edge Cascade
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)

ret, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)

contours, hierarchies = cv.findContours(
    thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('Contours', blank)

cv.waitKey(0)
