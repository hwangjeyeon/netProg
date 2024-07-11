from socket import *
import threading

port = 2500
BUFSIZE = 1024

def echoTast(sock):
    while True:
        data = sock.recv(BUFSIZE)
        if not data:
            break
        print('Received message:',data.decode())
        sock.send(data)
    
    sock.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

while True:
    conn, (remotehost, remoteport) = sock.accept()
    print('connected by', remotehost, remoteport)
    th = threading.Thread(target=echoTast, args=(conn,))
    th.start()