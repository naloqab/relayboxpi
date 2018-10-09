import socket

Host = '192.168.1.252'
Port = 5008

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host, Port))
s.sendall('LockStatus')
data = s.recv(1024)
s.close()