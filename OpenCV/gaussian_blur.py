import cv2 as cv

pic = cv.imread('road.jpg')
resize = cv.resize(pic,(480,240))
gray = cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(9,39),0)
cv.imshow('ORIGINAL',resize)
cv.imshow('gray',gray)
cv.imshow('blur',blur)
cv.waitKey(0)
cv.destroyAllWindows()
