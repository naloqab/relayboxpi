import RPi.GPIO as GPIO


RelayStatusFile = open('/var/www/RelayStatusFile.txt', 'r')
StatusArrayData = RelayStatusFile.read()
RelayStatusFile.close()

LockStatusFile = open('/var/www/ReceivedLockStatus.txt', 'r')
LockStatus = LockStatusFile.readline()
LockStatusFile.close()

GamingPCStatusFile = open('/var/www/GamingPCPowerStatus.txt', 'r')
GamingPCStatus = GamingPCStatusFile.readline()
GamingPCStatusFile.close()

StatusArray = []

StatusArray.append(StatusArrayData[1])
StatusArray.append(StatusArrayData[4])
StatusArray.append(StatusArrayData[7])
StatusArray.append(StatusArrayData[10])
StatusArray.append(StatusArrayData[13])
StatusArray.append(StatusArrayData[16])
StatusArray.append(StatusArrayData[19])
StatusArray.append(StatusArrayData[22])
StatusArray.append(LockStatus)
StatusArray.append(GamingPCStatus)

x = 0
while x < 8:
	if StatusArray[x] == '1':
		print 'OFF'
	else:
		print 'ON'
	x += 1

print StatusArray[8]
print StatusArray[9]