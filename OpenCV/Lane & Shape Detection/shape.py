import cv2
import numpy as np

def find_shapes(img,lower_color,upper_color, n_sides):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    blurred = cv2.GaussianBlur(mask, (5,5), 0)
    # edges = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(blurred, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    shapes = []

    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02*perimeter, True)
        if len(approx) == n_sides:
            shapes.append(approx)
    
    return shapes

cap = cv2.VideoCapture(0)

#Define colour thresholds
lower_color = np.array([86,75,96])
upper_color = np.array([179,255,255])

while True:
    ret, frame = cap.read()

    shapes = find_shapes(frame, lower_color, upper_color, 4)

    for shape in shapes:
        cv2.drawContours(frame, [shape], 0, (0,255,0), 3)
    
    cv2.imshow('Colour Shape Traching', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()