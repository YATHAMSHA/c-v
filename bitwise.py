import cv2 as cv
from cv2 import bitwise_and
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)


bitwise =cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise', bitwise)

bitwiseor =cv.bitwise_or(rectangle,circle)
cv.imshow('or', bitwiseor)

xor =cv.bitwise_xor(rectangle,circle)

cv.imshow('xor', xor)

notoper =cv.bitwise_not(rectangle)
cv.imshow('not oper', notoper)



cv.waitKey(0).
