
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="127.0.0.1"
port =8000
s.connect((host,port))

while True:
    s.send('wellcome to 127 connect SpiderHost'.encode()) 
    
    data = s.recv(1024).decode()
    print (data)


s.close ()
