from socket import *
import os

BUF_SIZE = 1024
LENGTH = 4

sock = create_server(('', 7777), family=AF_INET, backlog=10)

while True:
    conn, addr = sock.accept()

    msg = conn.recv(BUF_SIZE)
    if not msg:
        conn.close()
        continue
    elif msg != b'Hello':
        conn.close()
        continue
    else:
        print(addr, msg.decode())
    
    conn.send(b'Filename')

    msg = conn.recv(BUF_SIZE)
    if not msg:
        conn.close()
        continue
    filename = msg.decode()
    try:
        filesize = os.path.getsize(filename)
    except:
        conn.send(b'Nofile')
        conn.close()
        continue
    else:
        fs_binary = filesize.to_bytes(LENGTH, 'big')
        conn.send(fs_binary)
    
    f = open(filename, 'rb')
    data = f.read()
    conn.sendall(data)

    msg = msg.recv(BUF_SIZE)
    if not msg:
        pass
    else:
        print(addr, msg.decode())
    
    f.close()
    conn.close()
