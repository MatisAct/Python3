
import socket
import sys

s = socket.socket()
host = socket.gethostname() 
port = 2004
s.connect((host,port))

while True:
    

    
        
    data = s.recv(1024).decode()
    print data
    
    sea=raw_input("your messenger-->")
    s.send('Client B:'+sea)   
    
s.close()
