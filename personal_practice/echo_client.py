import socket

port = int(input('port no:'))
address = ('localhost', port)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

while True:
    msg = input()
    s.send(msg.encode())
    data = s.recv(BUFSIZE)
    print('%s' % data.decode())

s.close()
