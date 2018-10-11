import socket
import time
import os

Host = ''
Port = 5007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((Host, Port))
s.listen(1)

while 1:
	data = ''
	print "\nWaiting for client to connect..\n"
	conn, Address = s.accept()
	print Address, "is connected."

    	data = conn.recv(1024)
	print "Data received:", data, "\n"
	

	if data == '0':
		if time.localtime().tm_hour >= 20 or time.localtime().tm_hour < 5:
			if time.localtime().tm_hour >= 23 or time.localtime().tm_hour < 5:
				os.system("sudo python /var/www/Relay1ON.py")

				os.system("sudo python /var/www/Relay2ON.py")

			else:
				os.system("sudo python /var/www/AllRelaysON.py")

	if data == '1':
		os.system("sudo python /var/www/AllRelaysOFF.py")


	if data == 'Locked' or data == 'Unlocked':
		LockStatus = data
		StatusFile = open('/var/www/ReceivedLockStatus.txt', 'w')
		StatusFile.write(LockStatus)
		StatusFile.close()

	conn.close()