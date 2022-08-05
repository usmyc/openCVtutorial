import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('1.jpeg')


# cv.imshow('Image', img)
# plt.imshow(img)
# plt.show()

b, g, r = cv.split(img)



merged = cv.merge([b,g,r])
cv.imshow('merged', merged)


# #BGR to HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)


cv.waitKey(0)
