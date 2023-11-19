#####################
#                   #
#   Team: Top-Gun   #
#                   #
#####################

import RPi.GPIO as GPIO
import time
in1 = 25 #17
in2 = 8 #27
in3 = 7 #5
in4 = 1 #6
rightSensor = 6
leftSensor = 5
en1 = 12
en2 =13
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(rightSensor,GPIO.IN)
GPIO.setup(leftSensor,GPIO.IN)
GPIO.setup(en1, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
GPIO.output(in1,0)
GPIO.output(in2,0)
GPIO.output(in3,0)
GPIO.output(in4,0)
l= GPIO.PWM(en1,1000)
l.start(100)
r= GPIO.PWM(en2,1000)
r.start(20)
# Move left
def turnleft():
    #stopAll()
    time.sleep(0.01)
    GPIO.output(in1,1)
    GPIO.output(in2,0)
    GPIO.output(in3,0)
    GPIO.output(in4,0)
    r.ChangeDutyCycle(100)
    l.ChangeDutyCycle(100)
    print('l')
# Move right
def turnright():
    GPIO.output(in1,0)
    GPIO.output(in2,0)
    GPIO.output(in3,1)
    GPIO.output(in4,0)
    print('r')
    #r.ChangeDutyCycle(100)
    time.sleep(0.025)
    
    r.ChangeDutyCycle(30)
    l.ChangeDutyCycle(100)
    
# Move forward
def forward():
    l.ChangeDutyCycle(80)
    r.ChangeDutyCycle(16)
    GPIO.output(in1,1)
    GPIO.output(in2,0)
    GPIO.output(in3,1)
    GPIO.output(in4,0)
    print('f')

def back():
    l.ChangeDutyCycle(80)
    r.ChangeDutyCycle(16)
    GPIO.output(in1,0)
    GPIO.output(in2,1)
    GPIO.output(in3,0)
    GPIO.output(in4,1)
    print('b')
# turn off all motors
def stopAll():
    #p.ChangeDutyCycle(65)
    #p1.ChangeDutyCycle(65)
    GPIO.output(in1,0)
    GPIO.output(in2,0)
    GPIO.output(in3,0)
    GPIO.output(in4,0)
    print('stop')
# main program loop
while True:
    if GPIO.input(leftSensor)==1 and GPIO.input(rightSensor) == 1:
        stopAll()
    if GPIO.input(leftSensor)==0 and GPIO.input(rightSensor)==0:
        forward()
    if GPIO.input(leftSensor)==0 and GPIO.input(rightSensor)==1:
        back()
        time.sleep(0.02)
        r.ChangeDutyCycle(90)
        #time.sleep(0.001)
        while GPIO.input(leftSensor)==0 and GPIO.input(rightSensor)==1:
            turnright()
            time.sleep(0.06)
    if GPIO.input(leftSensor)==1 and GPIO.input(rightSensor)==0:
        back()
        time.sleep(0.02)
        turnleft()
        time.sleep(0.1)
GPIO.cleanup()