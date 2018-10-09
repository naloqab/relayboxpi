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

GPIO.output(2, False)
GPIO.output(3, False)
GPIO.output(4, False)
GPIO.output(17, False)
#GPIO.output(27, False)
#GPIO.output(14, False)
#GPIO.output(15, False)
#GPIO.output(18, False)
