import cv2 as cv
import numpy as np

with open('imgText.md', 'w') as imgText:
    img = cv.imread('2.jpg')
    imgText.write(str(img))
