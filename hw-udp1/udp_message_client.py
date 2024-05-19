import socket


SERVER_IP = 'localhost'
SERVER_PORT = 3333
BUFFER_SIZE = 1024


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_message(message):
    client_socket.sendto(message.encode('utf-8'), (SERVER_IP, SERVER_PORT))
    data, _ = client_socket.recvfrom(BUFFER_SIZE)
    print(data.decode('utf-8'))

while True:
    command = input("Enter the message(\"send mboxId message\" or \"receive mboxId\"): ")
    send_message(command)
    if command.strip() == "quit":
        break

client_socket.close()
