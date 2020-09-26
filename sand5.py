import numpy as np
import cv2 as cv

img = np.zeros((512, 512, 3), np.uint8)

#rectangle
cv.rectangle(img, (128, 0), (510, 255), (0, 255, 0), 3)

#circle
cv.circle(img, (255, 255), 100, (0, 0, 255), 5)

#text 
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'LOL RACHIT GAY!!', (255, 255), font, 1, (0, 0xFF, 0xFF), 2, cv.LINE_AA)

cv.imshow('Image', img)
cv.waitKey(0)