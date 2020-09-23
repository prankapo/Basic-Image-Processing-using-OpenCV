import numpy as np
import cv2 as cv

img = np.zeros((512, 512, 3), np.uint8)
var = 0
for row in img :
    var = var + 1
    print(var, row)
img = cv.line(img, (0,0), (511, 511), (255, 255, 0), 5)
cv.imshow('PK', img)

k = cv.waitKey(0)