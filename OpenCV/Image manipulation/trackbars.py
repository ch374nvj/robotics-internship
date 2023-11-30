#####################
#                   #
#   Team: Top-Gun   #
#                   #
#####################

import cv2 as cv
import numpy as np

def nothing(x):
    pass

cv.namedWindow('trackbars')
cv.resizeWindow('trackbars',(480,400))

cv.createTrackbar('huelower','trackbars',50,179,nothing)
cv.createTrackbar('huehigher','trackbars',100,179,nothing)
cv.createTrackbar('huelower2','trackbars',50,179,nothing)
cv.createTrackbar('huehigher2','trackbars',100,179,nothing)

cv.createTrackbar('satlower','trackbars',50,255,nothing)
cv.createTrackbar('sathigher','trackbars',255,255,nothing)

cv.createTrackbar('vallower','trackbars',50,255,nothing)
cv.createTrackbar('valhigher','trackbars',255,255,nothing)

cam = cv.VideoCapture(0)

while True:
    ret,frame = cam.read()
   # frame = cv.imread('stripes.jpg')
    rframe = cv.resize(frame,(480,240))
    cv.imshow("original",rframe)
    hsv = cv.cvtColor(rframe,cv.COLOR_BGR2HSV)

    HL = cv.getTrackbarPos('huelower','trackbars')
    HU = cv.getTrackbarPos('huehigher','trackbars')
    HL2 = cv.getTrackbarPos('huelower2','trackbars')
    HU2 = cv.getTrackbarPos('huehigher2','trackbars')

    SL = cv.getTrackbarPos('satlower','trackbars')
    SH = cv.getTrackbarPos('sathigher','trackbars')

    VL = cv.getTrackbarPos('vallower','trackbars')
    VH = cv.getTrackbarPos('valhigher','trackbars')

    l_b = np.array([HL,SL,VL])
    u_b = np.array([HU,SH,VH])
    l_b2 = np.array([HL2,SL,VL])
    u_b2 = np.array([HU2,SH,VH])

    FGmask = cv.inRange(hsv,l_b,u_b)
    FGmask2 = cv.inRange(hsv,l_b2,u_b2)
    FGmaskcomp = cv.add(FGmask,FGmask2)
    rFGmaskcomp = cv.resize(FGmaskcomp,(480,240))
    cv.imshow("FGmask",rFGmaskcomp)

    FG = cv.bitwise_and(rframe,rframe,mask = FGmaskcomp)
    cv.imshow("FG",FG)

    BGmask = cv.bitwise_not(rFGmaskcomp)
    cv.imshow("BG",BGmask)

    BG = cv.cvtColor(BGmask,cv.COLOR_GRAY2BGR)
    final = cv.add(FG,BG)

    cv.imshow('final',final)
    if cv.waitKey(1) & 0xff == ord('q'):
        break
cv.destroyAllWindows()