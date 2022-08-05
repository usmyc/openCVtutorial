import cv2 as cv
from cv2 import COLOR_BGR2GRAY
img = cv.imread('team.jpg')
cv.imshow('Real', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Real', gray)

haar_cascade = cv.CascadeClassifier('haardetected.xml')

faces_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=6)

print(f'number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow('Detected', img)

cv.waitKey(0)
