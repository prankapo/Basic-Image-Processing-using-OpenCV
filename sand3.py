import numpy as np
import cv2 as cv

'Create a black image'
img = np.zeros((512, 512, 3), np.uint8)

'Change color of image'
img[120:121] = [0, 0xFF, 0]

cv.imshow('Hola!!', img)
k = cv.waitKey(0)