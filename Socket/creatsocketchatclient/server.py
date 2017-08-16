
import socket 
from thread import *
import re
 

host = '0.0.0.0' 
port = 2004 
 

sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # khai báo hàm này là bắt buộc
sever.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # i don't know it T.T

sever.bind((host, port)) # creat sever with ip and port 

sever.listen(5) 
 
def clientthread(conn): # function input and output messenger

     while True:
         conn.send(' ') 

         data = conn.recv(1024) # input data in client
       
         print data
        

while True: # usually true , when client connect !



    conn, (ip,port) = sever.accept() # conn: data text, ip port : number exam:128.120...
    print ("wellcome to "+ip+" connecting server! ! !") # wellcome to client connect : clap clap:
    start_new_thread(clientthread,(conn,)) # let's go to function

 
conn.close()
sever.close()
