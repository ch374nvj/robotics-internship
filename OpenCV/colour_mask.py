#####################
#                   #
#   Team: Top-Gun   #
#                   #
#####################

import cv2
import numpy as np
img=cv2.imread("img.jpg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lw_green=np.array([0,50,50])
up_green=np.array([5,255,255])
mask=cv2.inRange(hsv,lw_green,up_green)
result=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("original",img)
cv2.imshow("green",result)
cv2.waitKey(0)
cv2.destroyAllWindow()