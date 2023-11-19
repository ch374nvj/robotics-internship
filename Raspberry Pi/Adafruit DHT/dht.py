#####################
#                   #
#   Team: Top-Gun   #
#                   #
#####################


import Adafruit_DHT
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
pin = 17 
sensor = Adafruit_DHT.DHT11
GPIO.setmode(GPIO.BCM) #set pi pinmode to BCM

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor.pin) #Read realtime values of temperature from DHT sensor
        if humidity is not None and temperature is not None:
            print(f"Temperature = {temperature:.1f}C, Humidity = {humidity:.1f}%")
        else:
            print("failed to read data from sensor")
            time.sleep(2) #Delay of 2 seconds

except KeyboardInterrupt:
    pass

GPIO.cleanup
