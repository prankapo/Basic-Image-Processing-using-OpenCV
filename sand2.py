import cv2 as cv
import numpy as np

img = cv.imread('p1.jpg')
cv.imshow('P.K.', img)

dimensions = img.shape
height = img.shape[0]
width = img.shape[1]
channel = img.shape[2]

print('Image dimensions: ', dimensions)
print('Image height: ', height)
print('Image width: ', width)
print('Number of channels: ', channel)
k = cv.waitKey(0)