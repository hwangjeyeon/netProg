import socket

port = 2500
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input()
    if msg == 'q':
        break
    sock.sendto(msg.decode(), ('localhost', port))
    data, addr = sock.recvfrom(BUFFSIZE)
    print(data.decode())

sock.close()