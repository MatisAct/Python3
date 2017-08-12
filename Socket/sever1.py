
import socket
s= socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
for x in range(4):
	while True:
		
	    c, addr = s.accept() 
	    print addr,':'
		a=raw_input('you:->')
		c.send(a)
c.close()		
