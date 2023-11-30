#####################
#                   #
#   Team: Top-Gun   #
#                   #
#####################

import cv2 as cv
import numpy as np
pic = cv.imread('road.jpg')
resize = cv.resize(pic,(600,600))
gray = cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(3,3),0)
edges = cv.Canny(blur,threshold1 = 120, threshold2 = 180)

lines = cv.HoughLinesP(edges, rho = 2, theta = np.pi/180, threshold = 150, 
                       minLineLength = 23, maxLineGap = 1)
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(resize,(x1,y1),(x2,y2),(0,0,255),2)
cv.imshow('Hough Line',resize)
cv.waitKey(0)
cv.destroyAllWindows()