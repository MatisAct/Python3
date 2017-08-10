# server.py
import socket

s = socket.socket()
host ='127.0.0.1'
port = 1234
s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept() # c là địa các thông điệp sever dưới dạng text, còn addr là đia chỉ ip và port connect
    print 'Got connection from', addr # in ra địa chỉ khi có ip đăng nhập vào
    c.send('Thank you for your connecting and fucking address your ip')  #gửi lại lời nhắn tới client

    c.close()
