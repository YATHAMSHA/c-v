import cv2 as cv

img =  cv.imread('photos/img2.8.png')

cv.imshow('yat', img)

cv.waitKey(0)

capture = cv.VideoCapture('videos/video5.mov')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('s'): break

capture.release()
cv.destroyAllWindows()