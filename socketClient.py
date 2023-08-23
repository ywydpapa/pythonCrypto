import socket
import random
from cryptography.fernet import Fernet
from key import mykey

key = mykey

fernet = Fernet(key)

server_ip = '192.168.108.131'
server_port = 1199

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((server_ip, server_port))

cnt = 0
while cnt < 15000:
    msg = ''
    msg = str(random.randrange(10,99))
    print(msg)
    msg = fernet.encrypt(msg.encode())
    print(msg)
    print('Count:',cnt)
#    dmsg = len(msg)
#    print(dmsg)
    socket.sendall(msg)
#    data = socket.recv(100)
#    msg = data.decode()
#    print('echo msg:', msg)
#    ent = '\n'
#    socket.sendall(ent.encode(encoding='utf-8'))
    cnt = cnt+1
msg = '/end'
socket.sendall(msg.encode(encoding='utf-8'))
print(msg)
socket.close()