import socket
import os

host = '192.168.1.100'
socketPort = 5009

command = b"GamingPCPowerStatus"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, socketPort))
s.sendall(command)
data = s.recv(1024)
s.close()

PowerStatus = data.decode('ascii')

logPath = '/var/www/GamingPCPowerStatus.txt'

if not os.path.exists(logPath):
    os.system("touch {}".format(logPath))

StatusFile = open(logPath, 'w')
StatusFile.write(PowerStatus)
StatusFile.close()
