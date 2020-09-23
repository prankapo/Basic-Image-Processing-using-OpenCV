import numpy as np
import cv2 as cv

img = np.zeros((512, 512, 3), np.uint8)
cv.line(img, (0, 0), (255, 255), (255, 0, 0), 5)
cv.line(img, (255, 255), (0, 511), (0, 255, 0), 5)
cv.line(img, (255, 255), (511, 0), (0, 0, 255), 5)
cv.line(img, (255, 255), (511, 511), (128, 0, 255), 5)

cv.imshow('IMAGE', img)
k = cv.waitKey(0)