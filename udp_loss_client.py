from socket import *

BUFF_SIZE = 1024
port = 5555

c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock = socket(('localhost', port))

for i in range(10):
    time= 0.1
    data= 'Hello IoT'
    while True:
        c_sock.send(data.encode())
        c_sock.settimeout(time)
        try:
            data = c_sock.recv(BUFF_SIZE)
        except timeout:
            time *= 2
            if time > 2.0:
                break
        else:
            print(data.decode())
            break
        