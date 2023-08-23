import socket, time,threading
from cryptography.fernet import Fernet
from key import mykey

key = mykey

fernet = Fernet(key)

host = '192.168.108.131'
port = 1199

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((host, port))

server_socket.listen()

print('echo server start')

client_soc, addr = server_socket.accept()

print('connected client addr:', addr)

# row = []

data = ''
cnt = 0

while True:
    data = client_soc.recv(100)
    msg = data.decode(encoding='utf-8')
    if len(msg)!= 0:
#        print(data)
#        print(msg)
#        print(len(msg))
        print("-----")
        if len(msg) == 100:
            dmsg = fernet.decrypt(data).decode('utf-8')
            print('No:',cnt)
            print('Decrypt Message:', dmsg)
            cnt = cnt + 1
    elif len(msg) == 4:
        break
    else:
        pass

time.sleep(1)
server_socket.close()
