from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('wating...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break

        try:
            rsp = eval(data.decode().strip())

        except:
            client.send(b'Try again')
        else:
            client.send(rsp.to_bytes(4,'big'))
    client.close()

    