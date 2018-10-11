import RPi.GPIO as GPIO

import os
import time

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

StatusArray = ["", "", "", "", "", "", "", ""]

while 1:
	time.sleep(10)
	
	StatusArray[0] = GPIO.input(2)
	StatusArray[1] = GPIO.input(3)
	StatusArray[2] = GPIO.input(4)
	StatusArray[3] = GPIO.input(17)
	StatusArray[4] = GPIO.input(27)
	StatusArray[5] = GPIO.input(14)
	StatusArray[6] = GPIO.input(15)
	StatusArray[7] = GPIO.input(18)

	RelayStatusFile = open('/var/www/RelayStatusFile.txt', 'w')
	RelayStatusFile.write(str(StatusArray))
	RelayStatusFile.close()