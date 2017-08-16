
import socket
import sys

s = socket.socket()
host = socket.gethostname() 
port = 2004
s.connect((host,port))

while True:
    

    
        
    
    sea=raw_input("<--your messenger-->")
    s.send('Client A:'+sea)
    data = s.recv(1024).decode()
    print (data)
s.close()
