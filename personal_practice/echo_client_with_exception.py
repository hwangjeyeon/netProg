import socket

port = int(input('port no:'))
address = ('localhost', port)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

while True:
    msg = input()
    try:
        byteSent = s.send(msg)
    except:
        break
    else:
        print('{}'.format(byteSent))

    try:
        data = s.recv(BUFSIZE)
    except:
        break
    else:
        if not data:
            break
        print(data.decode())
s.close()
