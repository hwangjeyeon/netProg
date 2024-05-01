from socket import *
import base64

def handle_request(request):
    request_line = request[0]
    filename = request_line.split()[1][1:]
    if not filename == 'index.html':
        response = 'HTTP/1.1 404 Not Found\r\n\r\n<html><title>Not Found</title><body>Not Found</body></html>'.encode()
        return response
    
    
    try:
        if filename == "index.html":
            mimeType = 'text/html'
            image = base64.b64encode(open('iot.png', 'rb').read()).decode()
            favicon = base64.b64encode(open('favicon.ico', 'rb').read()).decode()

        
            response_body = '''
                <html>
                <head>
                    <title>My Web Server</title>
                    <link rel="icon" href="data:image/x-icon;base64,{}">
                </head>
                <body>
                    <h1>사물인터넷학과에 홈페이지 오신것을 환영합니다</h1>
                    <p>저는 사물인터넷학과 19학번 황제연입니다.</p>
                    <div>
                        <img src="data:image/png;base64,{}">
                        사물인터넷학과 캐릭터
                    </div>
                </body>
                </html>
            '''.format(favicon, image).encode('euc-kr')

            response_header = 'HTTP/1.1 200 OK\r\nContent-Type:  {}\r\n\r\n'.format(mimeType).encode()
            response = response_header + response_body

    except FileNotFoundError:
        response = 'HTTP/1.1 404 Not Found\r\n\r\n<html><title>Not Found</title><body>Not Found</body></html>'.encode()

    return response

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80))
s.listen(10)
print('Waiting for connections...')

while True:
    client_socket, addr = s.accept()
    print('Connection from', addr)
    data = client_socket.recv(1024)
    if not data:
        break

    msg = data.decode()
    request = msg.split("\r\n")
    response = handle_request(request)
    client_socket.send(response)
    client_socket.close()
