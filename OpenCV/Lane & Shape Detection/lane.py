import cv2
import numpy as np

curveList =[]
avgVal = 10


def thresholding(img,lowerWhite,upperWhite):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowerWhite = np.array(lowerWhite)
    upperWhite = np.array(upperWhite)
    maskWhite = cv2.inRange(imgHSV,lowerWhite,upperWhite)
    return maskWhite

def imgWarp(img, points, w,h):
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    warped = cv2.warpPerspective(img,matrix,(w,h))
    return warped

def nothing(x):
    pass

def initializeTrackbarsHSV(initialTrackbarVals, centerLimit=5):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 480, 400)
    cv2.createTrackbar('huelower','Trackbars',initialTrackbarVals[0][0],179,nothing)
    cv2.createTrackbar('huehigher','Trackbars',initialTrackbarVals[0][1],179,nothing)

    cv2.createTrackbar('satlower','Trackbars',initialTrackbarVals[1][0],255,nothing)
    cv2.createTrackbar('sathigher','Trackbars',initialTrackbarVals[1][1],255,nothing)

    cv2.createTrackbar('vallower','Trackbars',initialTrackbarVals[2][0],255,nothing)
    cv2.createTrackbar('valhigher','Trackbars',initialTrackbarVals[2][1],255,nothing)

    cv2.createTrackbar('centerLimit','Trackbars',centerLimit,100,nothing)
    

def getTrackbarsHSV():
    HL = cv2.getTrackbarPos('huelower','Trackbars')
    HU = cv2.getTrackbarPos('huehigher','Trackbars')

    SL = cv2.getTrackbarPos('satlower','Trackbars')
    SU = cv2.getTrackbarPos('sathigher','Trackbars')

    VL = cv2.getTrackbarPos('vallower','Trackbars')
    VU = cv2.getTrackbarPos('valhigher','Trackbars')
    lower = [HL,SL,VL]
    upper = [HU,SU,VU]

    return lower,upper

def initializeTrackbarsPoints(intialTracbarVals,wT=480, hT=240):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Width Top", "Trackbars", intialTracbarVals[0],wT//2, nothing)
    cv2.createTrackbar("Height Top", "Trackbars", intialTracbarVals[1], hT, nothing)
    cv2.createTrackbar("Width Bottom", "Trackbars", intialTracbarVals[2],wT//2, nothing)
    cv2.createTrackbar("Height Bottom", "Trackbars", intialTracbarVals[3], hT, nothing)
    
def getTrackbarsPoints():
    pts = [
        cv2.getTrackbarPos("Width Top", "Trackbars"),
        cv2.getTrackbarPos("Height Top", "Trackbars"),
        cv2.getTrackbarPos("Width Bottom", "Trackbars"),
        cv2.getTrackbarPos("Height Bottom", "Trackbars"),
    ]
    return pts

def valTrackbarsPoints(wT=480, hT=240,pts=[0,0,0,240]):
    widthTop, heightTop, widthBottom, heightBottom = pts
    points = np.float32([(widthTop, heightTop), (wT-widthTop, heightTop), (widthBottom , heightBottom ), (wT-widthBottom, heightBottom)])
    return points

def plotPoints(img,points):
    for x in range(4):
        cv2.circle(img,(int(points[x][0]),int(points[x][1])),15,(0,0,255),cv2.FILLED)
    return img


def getLaneCurve(img,display=1,region=0.2,intialTrackBarVals=[0,0,0,240],centerLimit=5):
    imgResult = img.copy()
    lowerWhite, upperWhite = getTrackbarsHSV()
    imgThresh = thresholding(img,lowerWhite,upperWhite)
    h,w,c = img.shape
    # points = valTrackbarsPoints(pts=getTrackbarsPoints())
    points = valTrackbarsPoints()
    warp = imgWarp(imgThresh,points,w,h)
    warpPoints = plotPoints(img,points) 
    
    middlePoint,imgHist = getHistogram(warp,display=True,minPer=0.5,region=4)
    curveAveragePoint, imgHist = getHistogram(warp, display=True, minPer=0.9)
    curveRaw = curveAveragePoint - middlePoint
    
    # cv2.imshow('Threshold',imgThresh)
    # cv2.imshow('Warped',imgWarp)
    
    # return warp
    curveList.append(curveRaw)
    if len(curveList)>avgVal:
        curveList.pop(0)
    curve = int(sum(curveList)/len(curveList))
    
    if display != 0:
        imgInvWarp = imgWarp(warp, points, w, h)
        imgInvWarp = cv2.cvtColor(imgInvWarp, cv2.COLOR_GRAY2BGR)
        imgInvWarp[0:int(h * (1-region)), 0:w] = 0, 0, 0    ### Here you adjust the region of interest from cam feed
        imgLaneColor = np.zeros_like(img)
        imgLaneColor[:] = 0, 255, 0
        imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
        imgResult = cv2.addWeighted(imgResult, 1, imgLaneColor, 1, 0)
        midY = 450
        if curve <= centerLimit and curve >= -centerLimit:
            cv2.putText(imgResult, str(curve)+' Center', (h // 2 - 80, 85), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0), 3)
        elif curve >= centerLimit:
            cv2.putText(imgResult, str(curve)+' Right', (h // 2 - 80, 85), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 3)
        elif curve <= -centerLimit:
            cv2.putText(imgResult, str(curve)+' Left', (h // 2 - 80, 85), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 3)


        cv2.line(imgResult, (w // 2, midY), (w // 2 + (curve * 3), midY), (255, 0, 255), 5)
        cv2.line(imgResult, ((w // 2 + (curve * 3)), midY - 25), (w // 2 + (curve * 3), midY + 25), (0, 255, 0), 5)
        for x in range(-30, 30):
            w = w // 20
            cv2.line(imgResult, (w * x + int(curve // 50), midY - 10),
                     (w * x + int(curve // 50), midY + 10), (0, 0, 255), 2)

        #fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
        #cv2.putText(imgResult, 'FPS ' + str(int(fps)), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (230, 50, 50), 3);

    if display == 2:
        imgStacked = stackImages(1, ([warp,imgHist],[imgLaneColor, imgResult]))
        cv2.imshow('ImageStack', imgStacked)
    elif display == 1:
        cv2.imshow('Resutlt', imgResult)

    #### NORMALIZATION
    curve = curve/100
    if curve>1: curve ==1
    if curve<-1:curve == -1
 
    return curve



def getHistogram(img,minPer=0.1,display=False,region=1):
    
    if region == 1:
        histValues = np.sum(img, axis=0) #Histogram vector of image, column wise
    else:
        histValues = np.sum(img[img.shape[0]//region:,:], axis = 0)
    maxValue = np.max(histValues)
    minValue = minPer*maxValue
    indexArray = np.where(histValues >= minValue)
    basePoint = int(np.average(indexArray))

    if display:
        imgHist = np.zeros((img.shape[0],img.shape[1],3),np.uint8) # h = shape[0], w= shape[1]
        for x, intensity in enumerate(histValues):
            y = np.uint8(img.shape[0]-(intensity//255//region))
            # print(type(y))
            cv2.line(imgHist,(x,img.shape[0]),(x,y),(255,0,255),1)
            cv2.circle(imgHist,(basePoint,img.shape[0]),20,(0,255,255),cv2.FILLED)
        return basePoint,imgHist
    
    return basePoint, 0

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    # initializeTrackbarsPoints(intialTrackBarVals=[102, 80, 20, 214])
    initialTrackbarVals = [
        [46,179],   #Hue Limits
        [0,255],    #Saturation
        [0,170],    #Value
    ]
    initializeTrackbarsHSV(initialTrackbarVals)
    frameCounter = 0
    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0
 
        success, img = cap.read()
        img = cv2.resize(img,(480,240))
        centerLimit = cv2.getTrackbarPos('centerLimit','Trackbars')
        curve = getLaneCurve(img,display=2,centerLimit=centerLimit)
        if curve <= centerLimit and curve >= -centerLimit:
            print('Center')
        elif curve >= centerLimit:
            print('Right')
        elif curve <= -centerLimit:
            print('Left')

        
        # print(curve)
        # cv2.imshow('Vid',img)
        if cv2.waitKey(1) & 0xff ==ord("q"):
            cv2.destroyAllWindows()
            break