#!/usr/bin/python
# <------------- IMPORTS ----------------->
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import os
import requests
# <--------------------------------------->

# <----------- SENSOR TYPE --------------->
sensor = Adafruit_DHT.DHT22
# <--------------------------------------->

# <-------------- PINS ------------------->
pin_sensor = 15
fan = 14
light = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(light, GPIO.OUT)
GPIO.setup(fan, GPIO.OUT)

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
#pin = 23
# <--------------------------------------->

while True: 
   # <---------- SENSOR READING ------------->
   # Try to grab a sensor reading.  Use the read_retry method which will retry up
   # to 15 times to get a sensor reading (waiting 2 seconds between each retry).

   humidity, temperature = Adafruit_DHT.read_retry(sensor, pin_sensor)

   # Note that sometimes you won't get a reading and
   # the results will be null (because Linux can't
   # guarantee the timing of calls to read the sensor).
   # If this happens try again!
   # <--------------------------------------->
   if humidity is not None and temperature is not None:
      temperatura = '{0:0.1f}'.format(temperature)	    
      humedad = '{0:0.1f}'.format(humidity)
      print ("-------------------")
      print(humedad, temperatura)
      print ("-------------------")
      if (humidity>60):
         GPIO.output(fan,GPIO.HIGH)
      else:
         GPIO.output(fan,GPIO.LOW)

      if (temperature<26):
         GPIO.output(light,GPIO.HIGH)
      else:
         GPIO.output(light,GPIO.LOW)

      payload = {'temperatura': temperatura, 'humedad': humedad}
      requests.post("http://192.34.78.106", data=payload)
      #print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
   else:
      print('Failed to get reading. Try again!')
