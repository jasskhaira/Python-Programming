import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysok = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysok.connect((HOST,PORT))
mysok.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = mysok.recv(5120)
    if len(data) < 1 : break

    count = count + len(data)
    print(len(data),count)
    picture = picture + data

mysok.close()


pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode()   )

picture = picture[pos+4:]
fhand = open("stuff.jpg","wb")
fhand.write(picture)
fhand.close()