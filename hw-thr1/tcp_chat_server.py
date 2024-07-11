from socket import *
import threading
import time

clients = []

def handle_client(c_conn, c_addr):
    while True:
        msg = c_conn.recv(1024).decode()
        if msg == 'quit':
            print('exit', c_addr)


        if msg:
            print(f"{time.asctime()} {str(c_addr)} {msg}")
                
            for client in clients:
                if client != c_conn:
                    client.send(msg.encode())
        else:
            print(f"클라이언트 {c_addr} 연결 종료")
            c_conn.close()
            clients.remove(c_conn)
            break

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 2500))
s.listen(5)

print('Server Started')

while True:
    conn, addr = s.accept()
    print(f"new client: {addr}")

    clients.append(conn)

    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()
