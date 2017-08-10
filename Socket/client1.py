#client.py
import socket

s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host, port)) 
print s.recv(1024) # nhận size trả về kích thước 1mb
