from socket import *
import base64

def handle_request(request):
    request_line = request[0]
    filename = request_line.split()[1][1:]
    if not filename == 'index.html':
        response = 'HTTP/1.1 404 NOT FOUND\r\n\r\n'
        return response
    
    try:
        if filename == 'index.html':
            mimeType = 'text/html'
            image = base64.b64encode(open('iot.png', 'rb').read()).decode()
            favicon = base64.b64encode(open('favicon.pioc', 'rb').read()).decode()

            response_body = ''' '''.encode('euc-kr')

        response_header = 'HTTP/1.1 200 OK\r\nContent-Type: {}\r\n\r\n'.format(mimeType).encode()
        response = response_header + response_body

    except FileNotFoundError:
        response = 'HTTP/1.1 404 NOT FOUND\r\n\r\n'.encode()

    return response

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80))
s.listen(10)

while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    if not data:
        break

    msg = data.decode()
    request = msg.split('\r\n')
    response = handle_request(request)
    conn.send(response)
    conn.close()



