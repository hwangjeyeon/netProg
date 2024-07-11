import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9999))
s.listen(5)

while True:
    client, address = s.accept()
    client.send(time.ctime(time.time).encode())
    client.close()