import socket
import cv2
import numpy as np

BUF_SIZE = 8192
LENGTH = 10
videoFile = 'test.mp4'
sock = socket.create_server(('', 5000), family=socket.AF_INET, backlog=5)

while True:
    csock, addr = sock.accpet()
    cap = cv2.VideoCapture(videoFile)

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            temp = csock.recv(BUF_SIZE)
            if not temp:
                break

            result, imgEncode = cv2.imencode('.jpg', frame)
            data = np.array(imgEncode)
            byteData = data.tobytes()
            csock.send(str(len(byteData)).zfill(LENGTH).encode())

            temp = csock.recv(BUF_SIZE)
            if not temp:
                break

            csock.send(byteData)
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
    csock.close()