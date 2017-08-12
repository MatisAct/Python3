
import socket

s = socket.socket()
host ="127.0.0.1"
port =8000
s.connect((host,port))
for x in range(1000):
    while True:
        mess=input('nhap tin nhan:')

        s.send(mess.encode()) 
        
        data = s.recv(1024).decode()
        print ('admin>',data)
        
s.close ()
