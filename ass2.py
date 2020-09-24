import numpy as np
import cv2 as cv

'Create the background: background color + cross'
img = np.zeros((512, 512, 3), np.uint8)
cv.line(img, (0, 0), (256, 256), (0xFF, 0, 0), 5)
cv.line(img, (511, 0), (256, 256), (0, 0xFF, 0), 5)
cv.line(img, (0, 511), (256, 256), (0, 0, 0xFF), 5)
cv.line(img, (511, 511), (256, 256), (0xFF, 0, 0xFF), 5)
cv.rectangle(img, (0, 0), (511, 511), (0, 0xFF, 0xFF), 5)

'The alien with BOobs'
y_cord = 0
for i in range(0, 3):
    cv.circle(img, (256, y_cord), 100, (0xAA, 0xAA, 0xAA), 5)
    if i == 1:
        cv.circle(img, (0, y_cord), 100, (0xAA, 0xAA, 0xAA), 5)
        cv.circle(img, (511, y_cord), 100, (0xAA, 0xAA, 0xAA), 5)
    y_cord = (255 * (i + 1)) + 1
cv.imshow('ASS2', img)
cv.waitKey(0)