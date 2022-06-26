import cv2 as cv

img =  cv.imread('photos/img2.8.png')

cv.imshow('yat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 165)
cv.imshow('Canny', canny)

dilated = cv.dilate(canny, (7,7), iterations=2)
cv.imshow('Dilated', dilated)
cv.waitKey(0).
