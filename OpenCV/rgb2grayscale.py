import cv2 as cv

pic = cv.imread('road.jpg')
resized_pic = cv.resize(pic,(480,240))
gray = cv.cvtColor(resized_pic,cv.COLOR_BGR2GRAY)
cv.imshow('Original',resized_pic)
cv.imshow('Grayscaled',gray)
cv.waitKey(0)
cv.destroyAllWindows()
