import socket 
from threading import Thread 

 

class ClientThread(Thread): 
 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print ("[+] wellcome to  " + ip + ":" + str(port) +"connect to server ! ! ! !" )
 
    def run(self): 
        while True : 
            
            data = conn.recv(2048) #nhan tin nhan tu clients
            print (data)
            MESSAGE = raw_input("your messenger:")
            
            if MESSAGE == 'exit':
                break
            conn.send(MESSAGE)  # gui tn ve client 
 
# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '0.0.0.0' 
TCP_PORT = 2004 
BUFFER_SIZE = 20  # Usually 1024, but we need quick response 
 
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) # tao 1 sever voi ip va port nhu tren
threads = [] 
 
while True: 
    tcpServer.listen(5) 
    print ("\nWaiting for connections.........." )
    conn, (ip,port) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() # bat dau ham thread o tren
    threads.append(newthread) # in function new thread vao threads 
 
for t in threads: # reapeat class thong qua mang threads 
    t.join() 
