from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())

    # 여기서부터 이름 수신 및 출력
    name = client.recv(1024)
    print(name.decode())
    ## 학번 전송
    student_id = (20191511).to_bytes(4,'big')
    client.send(student_id)
    client.close()