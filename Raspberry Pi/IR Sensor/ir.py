#####################
#                   #
#   Team: Top-Gun   #
#                   #
#####################

import RPi.GPIO as GPIO
import time

TRIG = 15#GPIO4  - pin 7
ECHO = 18 #GPIO17 - pin 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    pulse_start = time.time()
    pulse_end = time.time()

    
    
    
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        
    #calculation part
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration*17150
    distance = round(distance,2)
    
    return distance

try:
    
    while True:
        distance = get_distance()
        print('Distance: {} cm'.format(distance))
        time.sleep(0.5)
        
        if input()=='q':
            break
except KeyboardInterrupt:
    pass

GPIO.cleanup()