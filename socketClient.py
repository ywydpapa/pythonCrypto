import socket
import pymysql
import random
from cryptography.fernet import Fernet
from key import mykey

key = mykey

fernet = Fernet(key)

server_ip = '192.168.108.140'
server_port = 1199

def dbins(query):
    db = pymysql.connect(host='192.168.108.102', user='swcore', password='core2020', db='vtekmon', charset='utf8')
    cur = db.cursor()
    cur.execute(query)
    db.commit()
#    db.close()

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((server_ip, server_port))

cnt = 0
while cnt < 5000:
    msg = ''
    emsg = ''
    msg = str(random.randrange(100,99999))
    msg = "AKEY"+str(msg)
    print(msg)
    emsg = fernet.encrypt(msg.encode())
    print(emsg)
    print('Count:',cnt)
#    dmsg = len(msg)
#    print(dmsg)
    socket.sendall(emsg)
    emsg = emsg.decode('utf-8')
#    emsg = emsg[:98]
    sql = "insert into cryptoProtocol (rowNum,sendData,encData,regDate) values (%i,'%s','%s', now())" % (cnt,msg,emsg)
    dbins(sql)

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


