import cv2 as cv

img = cv.imread('1.jpeg')
cv.imshow('Cat', img)

# # grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # blur
# blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# #Edge Cascade
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)

# #Dilating the image
# dilated = cv.dilate(canny, (3,3), iterations=1)
# cv.imshow('Dilated', dilated)

# #Eroding
# eroded= cv.erode(dilated, (7,7), iterations=1)
# cv.imshow('Eroded', eroded)

#Resize
resized = cv.resize(img, (500,500))
cv.imshow('Resized', resized)


cv.waitKey(0)
