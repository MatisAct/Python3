import socket


s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)

while True:
	
    c, addr = s.accept() 
    print 'Got connection from',addr
    a=raw_input('your messenger send to client:->')
    c.send(a)  

    c.close()
