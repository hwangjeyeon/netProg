import socket

port = 2500
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(('',port))

while True:
    msg, addr = sock.recvfrom(BUFSIZE)
    print(msg.decode())

    sock.sendto(msg, addr)
