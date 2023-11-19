#####################
#                   #
#   Team: Top-Gun   #
#                   #
#####################

import RPi.GPIO as GPIO
from time import sleep

IN1 = 17
IN2 = 27
en = 22
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(IN1,GPIO.LOW)
GPIO.output(IN2,GPIO.LOW)
p = GPIO.PWM(en,1000)
p.start(25)

try:
    while True:
        user_input = input("Enter 'F' for forward, and 'B' for backward. Enter 'Q' to quit: ").upper()
        if user_input == 'F':
            print("Forward")
            GPIO.output(IN1, GPIO.HIGH)
            GPIO.output(IN2, GPIO.LOW)
            p.ChangeDutyCycle(35)

        elif user_input == 'B':
            print("Backward")
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.HIGH)
        
        elif user_input == 'Q':
            break

except KeyboardInterrupt:
    pass

GPIO.cleanup()


