from socket import *

s = socket(AF_INET, SOCK_STREAM)
addr = ('localhost', 9000)
s.connect(addr)
name = 'Hwang Je Yeon'
s.send(name.encode())

# 주소 출력
msg = s.recv(1024)
print(msg.decode())

# 학번
student_id = s.recv(1024)
print(int.from_bytes(student_id,'big'))
s.close()