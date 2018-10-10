import sys
# import paramiko
import socket

host = '192.168.1.100'
socketPort = 5009
SSHPort = 22
username = 'pi'
password = 'Kaka2233!'

bootGamingPC = b"python3 /home/pi/code/bootGamingPC.py"
shutdownGamingPC = b"python3 /home/pi/code/shutdownGamingPC.py"

if sys.argv[1] == 'ON':
    try:
        # ssh = paramiko.SSHClient()
        # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh.connect(host, SSHPort, username, password)
        # stdin, stdout, stderr = ssh.exec_command(bootGamingPC)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, socketPort))
        s.sendall(bootGamingPC)
        data = s.recv(1024)
        s.close()

        PowerStatus = 'ON'
    except:
        PowerStatus = 'OFF'
else:
    try:
        # ssh = paramiko.SSHClient()
        # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh.connect(host, SSHPort, username, password)
        # stdin, stdout, stderr = ssh.exec_command(shutdownGamingPC)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, socketPort))
        s.sendall(shutdownGamingPC)
        data = s.recv(1024)
        s.close()

        PowerStatus = 'OFF'
    except:
        PowerStatus = 'ON'

StatusFile = open('/var/www/GamingPCPowerStatus.txt', 'w')
StatusFile.write(PowerStatus)
StatusFile.close()