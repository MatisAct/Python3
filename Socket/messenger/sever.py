import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 8000
print (host)
print (port)
serversocket.bind((host, port))

serversocket.listen(5)
print ('server started and listening')
while 1:
    (clientsocket, addr) = serversocket.accept()
    print ("da ket noi voi :!",addr)
    data = clientsocket.recv(1024).decode()
    print (data)
    r=input("typing:")
    clientsocket.send(r.encode())
