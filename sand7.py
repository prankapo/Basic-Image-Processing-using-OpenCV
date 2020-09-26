import numpy as np
import cv2 as cv

img = cv.imread('p1.jpg')
kernel = np.ones((5, 5), np.float32)/25
dst = cv.filter2D(img, -1, kernel)

erosion = cv.erode(img, kernel, iterations = -1)

cv.imshow('Original', img)
cv.imshow('Transplant', erosion)
cv.waitKey(0)