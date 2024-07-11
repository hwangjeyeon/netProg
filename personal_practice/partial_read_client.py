from socket import *

sock = create_connection(('localhost', 9999))

data_size = 20
rx_size = 0
total_data = []
while rx_size < data_size:
    data = sock.recv(4)
    if not data:
        break
    rx_size += len(data)
    total_data.append(data.decode())

message = ''.join(total_data)
print(message)
sock.close()