import cv2 as cv

vid = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',fourcc,20.0,(640,480))
while True:
    ret,frame = vid.read()
    cv.imshow('Video Feed',frame)
    #Start recording when 'p' key is pressed in the 'Video Feed' window
    if cv.waitKey(1) & 0xff == ord("p"):
        while True:
            out.write(frame)
            print("recording")
            ret,frame = vid.read()
            cv.imshow('video',frame)
            #Wait for 's' keypress, then pause recording
            if cv.waitKey(1) & 0xff == ord("s"):
                print("stopped")
                break
    # print("test")
    #Wait for 'q' keypress, then exit while loop
    if cv.waitKey(1) & 0xff ==ord("q"):
        print("ended")
        break

#Save the recorded video, and quit program    
vid.release()
cv.destroyAllWindows()