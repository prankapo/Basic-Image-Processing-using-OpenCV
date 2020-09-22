import numpy as np
import cv2 as cv

img = cv.imread("p1.jpg")
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)