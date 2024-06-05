import socket, select, time

clients = []

BUFFER = 1024
PORT = 2500

sock = socket.socket()
sock.bind(('', PORT))
sock.listen(5)

print('Server Started')
clients.append(sock)


while True:
    r_sock, w_sock, e_sock = select.select(clients, [],[])
    
    for s in r_sock:
        if s == sock:
            c_sock, addr = sock.accept()
            clients.append(c_sock)
            print('new client ', addr)
        else:
            data = s.recv(BUFFER)
            if not data or data.decode() == 'quit':
                clients.remove(s)
                s.close()
                break

            print(time.asctime() + str(addr) + ":" + data.decode())
            for client in clients:
                if client != sock and client != s:
                    client.send(data)
        
            
        
    
