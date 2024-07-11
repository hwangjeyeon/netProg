import socket, select

socks = []
BUFFER = 1024
PORT = 2500

s_sock = socket.socket()
s_sock.bind(('', PORT))


while True:
    r_sock, w_sock, e_sock = select.select(socks, [], [])

    for s in r_sock:
        if s == s_sock:
            c_sock, addr = s_sock.accept()
            socks.append(c_sock)
        else:
            data = s.recv(BUFFER)
            if not data:
                s.close()
                socks.remove(s)
                continue
            s.send(data)

