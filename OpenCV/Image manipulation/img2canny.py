#####################
#                   #
#   Team: Top-Gun   #
#                   #
#####################

import cv2 as cv
pic = cv.imread('road.jpg')
resize = cv.resize(pic,(480,240))
gray = cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(3,3),0)
edges = cv.Canny(blur,threshold1 = 150, threshold2 = 200)
cv.imshow('ORIGINAL',resize)
cv.imshow('gray',gray)
cv.imshow('blur',blur)
cv.imshow('Canny',edges)
cv.waitKey(0)
cv.destroyAllWindows()