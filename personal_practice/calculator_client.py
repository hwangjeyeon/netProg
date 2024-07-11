from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 2500))

while True:
    try:
        msg = input()
        if msg == 'q':
            break
        eval(msg)
    except:
        print('다시 입력하세요')
        continue   
    else:
        s.send(msg.encode())
    
    print(int.from_bytes(s.recv(1024), 'big'))

s.close()