from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 2500))
s.listen(3)

while True:
    client, addr = s.accpet()
    while True:
        data = client.recv(1024)
        if not data:
            break
        
        try:
            rsp = eval(data.decode().strip())
        except:
            client.send(b'Try Again')
        else:
            client.send(rsp.to_bytes(4, 'big'))
    
    client.close()