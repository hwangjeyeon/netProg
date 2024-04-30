from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    try:
        msg = input('계산식을 입력하세요')
        if msg == 'q':
            break
        eval(msg)
    except Exception:
        print('다시 입력하세요')
        continue
    else:
        
        s.send(msg.encode())

    print('Received message:', int.from_bytes(s.recv(1024),'big'))

s.close()
