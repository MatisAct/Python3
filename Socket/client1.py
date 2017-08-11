#client.py
import socket
for x in xrange(4):
	
	s = socket.socket()

	host = socket.gethostname()
	port = 1234

	s.connect((host, port)) 
	print s.recv(1024) 
	
