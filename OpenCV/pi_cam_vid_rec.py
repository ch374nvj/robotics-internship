#####################
#                   #
#   Team: Top-Gun   #
#                   #
#####################

import cv2 as cv


from picamera2 import Picamera2, Preview
cam=Picamera2()
camera_config = cam.create_preview_configuration()
cam.configure(camera_config)
cam.start()
cam.sensor_resolution=(640,480)
frame = cam.capture_array("main")


fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',fourcc,30.0,(640,480))
recording = False
while True:
    frame = cam.capture_array("main")
    frame = frame[:,:,:3]
    #print(frame)
    # ret,frame = vid.read()
    cv.imshow("Videoq",frame)
    key = cv.waitKey(1) & 0xff
    
    if key == ord("p"):
        recording = True
        print("Recording Started")
    elif key == ord('s'):
        recording = False
        print("Recording Stopped")
        
    if recording:
        out.write(frame)
    if not recording and key == ord("q"):
        break
    
# vid.release()
out.release()
cv.destroyAllWindows()