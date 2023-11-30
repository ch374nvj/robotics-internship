#####################
#                   #
#   Team: Top-Gun   #
#                   #
#####################

import cv2

stream =cv2.VideoCapture(0)

while True:
    reslt, img = stream.read()
    print(reslt)
    print(img)
    cv2.imwrite(filename='saved_img.jpg', img=img)
    #stream.release()
    img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_COLOR)
    img_new = cv2.imshow("Captured Image", img_new)
    cv2.waitKey(50)

stream.release()
cv2.destroyAllWindows() 