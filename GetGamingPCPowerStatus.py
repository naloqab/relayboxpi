import socket
import os
from time import sleep

host = '192.168.1.100'
socketPort = 5009

command = b"GamingPCPowerStatus"
data = False

logPath = '/var/www/GamingPCPowerStatus.txt'

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, socketPort))
        s.sendall(command)
        data = s.recv(1024)
        s.close()

    except Exception as e:
        print(str(e))

    if data:
        PowerStatus = data.decode('ascii')
    else:
        PowerStatus = "No response"


    if not os.path.exists(logPath):
        os.system("touch {}".format(logPath))

    StatusFile = open(logPath, 'w')
    StatusFile.write(PowerStatus)
    StatusFile.close()

    sleep(10)
