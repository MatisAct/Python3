import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 8000
print (host)
print (port)
server.bind((host, port))

server.listen(5)
print ('server started and listening')
while 1:
    (client, addr) = server.accept()
    print ("connecting  :!",addr)
    data = client.recv(1024).decode()
    print ('client>',data)
    r=input("you send:>")
    client.send(r.encode())
