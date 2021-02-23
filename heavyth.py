import numpy as np
import cv2 as cv

img = cv.imread("I1.jpg")
x = 10
kernel = np.ones((x, x), np.uint8)
perp_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, perp_thresh = cv.threshold(perp_gray, 128, 255, cv.THRESH_BINARY)
perp_morph = cv.erode(perp_thresh, kernel, iterations = 1)
#perp_morph = cv.GaussianBlur(perp_morph,(5,5),0)

cv.imshow("IMG", perp_morph)
cv.waitKey(0)
cv.imwrite("I2.jpg", perp_morph)