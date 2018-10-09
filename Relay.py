import sys
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#AllPinNumbers = [2, 3, 4, 17, 27, 14, 15, 18]
AllPinNumbers = [2, 3, 4, 17]

RelayNumber = sys.argv[1] # 1-8
RelayStatus = sys.argv[2] # ON or OFF


if RelayStatus == 'ON':
	PinStatus = False
elif RelayStatus == 'OFF':
	PinStatus = True
else:
	print ("\nIncorrect entry. Must be ON or OFF.")


if RelayNumber == '1':
	GPIO.setup(AllPinNumbers[0], GPIO.OUT)
	GPIO.output(AllPinNumbers[0], PinStatus)
elif RelayNumber == '2':
	GPIO.setup(AllPinNumbers[1], GPIO.OUT)
	GPIO.output(AllPinNumbers[1], PinStatus)
elif RelayNumber == '3':
	GPIO.setup(AllPinNumbers[2], GPIO.OUT)
	GPIO.output(AllPinNumbers[2], PinStatus)
elif RelayNumber == '4':
	GPIO.setup(AllPinNumbers[3], GPIO.OUT)
	GPIO.output(AllPinNumbers[3], PinStatus)
	
# elif RelayNumber == '5':
	# GPIO.setup(AllPinNumbers[4], GPIO.OUT)
	# GPIO.output(AllPinNumbers[4], PinStatus)
# elif RelayNumber == '6':
	# GPIO.setup(AllPinNumbers[5], GPIO.OUT)
	# GPIO.output(AllPinNumbers[5], PinStatus)
# elif RelayNumber == '7':
	# GPIO.setup(AllPinNumbers[6], GPIO.OUT)
	# GPIO.output(AllPinNumbers[6], PinStatus)
# elif RelayNumber == '8':
	# GPIO.setup(AllPinNumbers[7], GPIO.OUT)
	# GPIO.output(AllPinNumbers[7], PinStatus)
	
elif RelayNumber == 'All':
	for Pin in AllPinNumbers:
		GPIO.setup(Pin, GPIO.OUT)
		GPIO.output(Pin, PinStatus)
else:
	print ("\nIncorrect entry. Must be 1-8 or All.")