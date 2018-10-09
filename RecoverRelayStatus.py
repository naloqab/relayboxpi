import RPi.GPIO as GPIO


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

RelayStatusFile = open('/var/www/RelayStatusFile.txt', 'r')
StatusArrayData = RelayStatusFile.read()

GPIO.output(2, int(StatusArrayData[1]))
GPIO.output(3, int(StatusArrayData[4]))
GPIO.output(4, int(StatusArrayData[7]))
GPIO.output(17, int(StatusArrayData[10]))
GPIO.output(27, int(StatusArrayData[13]))
GPIO.output(14, int(StatusArrayData[16]))
GPIO.output(15, int(StatusArrayData[19]))
GPIO.output(18, int(StatusArrayData[22]))

RelayStatusFile.close()