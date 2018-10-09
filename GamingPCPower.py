import sys
import paramiko

ip = '192.168.1.100'
port = 22
username = 'pi'
password = 'Kaka2233!'

bootGamingPC = 'python3 code/bootGamingPC.py'
shutdownGamingPC = 'python3 code/shutdownGamingPC.py'
# bootGamingPC = 'echo bootTest'
# shutdownGamingPC = 'echo shutdownTest'

if sys.argv[1] == 'ON':
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, username, password)
        stdin, stdout, stderr = ssh.exec_command(bootGamingPC)
        PowerStatus = 'ON'
    except:
        PowerStatus = 'OFF'
else:
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, username, password)
        stdin, stdout, stderr = ssh.exec_command(shutdownGamingPC)
        PowerStatus = 'OFF'
    except:
        PowerStatus = 'ON'

StatusFile = open('/var/www/GamingPCPowerStatus.txt', 'w')
StatusFile.write(PowerStatus)
StatusFile.close()