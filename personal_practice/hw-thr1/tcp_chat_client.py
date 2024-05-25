import socket
import threading

def receive(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        print(message)

def send(client_socket):
    while True:
        message = input()
        client_socket.send(('['+my_id+'] '+message).encode())


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 2500))

my_id = input('ID를 입력하세요: ')


receive_thread = threading.Thread(target=receive, args=(s,))
receive_thread.start()

send_thread = threading.Thread(target=send, args=(s,))
send_thread.start()
