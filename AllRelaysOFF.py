import RPi.GPIO as GPIO

import os

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)


GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

GPIO.output(2, True)
GPIO.output(3, True)
GPIO.output(4, True)
GPIO.output(17, True)
#GPIO.output(27, True)
#GPIO.output(14, True)
#GPIO.output(15, True)
#GPIO.output(18, True)
