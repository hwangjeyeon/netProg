import socket
import threading


message_boxes = {}


SERVER_IP = 'localhost'
SERVER_PORT = 3333
BUFFER_SIZE = 1024


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

def handle_client(data, client_address):
    global message_boxes

    message = data.decode('utf-8').strip()
    if message.startswith("send"):
        parts = message.split(' ', 2)
        if len(parts) == 3:
            mboxID, msg = parts[1], parts[2]

            if mboxID not in message_boxes:
                message_boxes[mboxID] = []

            message_boxes[mboxID].append(msg)
            server_socket.sendto(b'OK', client_address)
    elif message.startswith("receive"):
        parts = message.split(' ', 1)

        if len(parts) == 2:
            mboxID = parts[1]
            if mboxID in message_boxes and message_boxes[mboxID]:
                msg = message_boxes[mboxID].pop(0)
                server_socket.sendto(msg.encode('utf-8'), client_address)
            else:
                server_socket.sendto(b'No messages', client_address)
    elif message == "quit":
        server_socket.close()
        exit(0)
    else:
        server_socket.sendto(b'Invalid command', client_address)

print(f"Server started at {SERVER_IP}:{SERVER_PORT}")
while True:
    data, client_address = server_socket.recvfrom(BUFFER_SIZE)
    threading.Thread(target=handle_client, args=(data, client_address)).start()
