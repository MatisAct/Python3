import socket
import sys

server = socket.socket()
host = "127.0.0.1"
port = 8000
print (host)
print (port)
server.bind((host, port))

server.listen(1000)
print ('waiting.....')

while True:
	(client, addr) = server.accept()
	print ("connecting  :!",addr)
	for x in range(5):
		data = client.recv(1024).decode()
		print ('client>',data)
		r=input("you send:>")
		client.send(r.encode())	
	if r=='bye':
		sys.exit(0)
		 
