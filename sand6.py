import cv2 as cv

img = cv.imread('p1.jpg')
cv.imshow('ORIGINAL', img)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Purani Picture', gray_img)

cv.waitKey(0)
cv.destroyAllWindows()