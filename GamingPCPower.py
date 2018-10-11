import sys
import socket

host = '192.168.1.100'
socketPort = 5009

bootGamingPC = b"python3 /home/pi/code/bootGamingPC.py"
shutdownGamingPC = b"python3 /home/pi/code/shutdownGamingPC.py"

if sys.argv[1] == 'ON':
    command = bootGamingPC
else:
    command = shutdownGamingPC

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, socketPort))
s.sendall(command)
data = s.recv(1024)
s.close()