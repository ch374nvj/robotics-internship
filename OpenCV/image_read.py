#####################
#                   #
#   Team: Top-Gun   #
#                   #
#####################

import cv2
pic = cv2.imread('road.jpg')
#rotate_pc = cv2.rotate(pic,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Image',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()