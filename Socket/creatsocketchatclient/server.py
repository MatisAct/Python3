
import socket 
from thread import *
import re
 

host = '0.0.0.0' 
port = 2004 
 

sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sever.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

sever.bind((host, port))

sever.listen(5) 
 
def clientthread(conn):

     while True:
         conn.send(' ') 

         data = conn.recv(1024) 
         if data=='bye':
        	 break
         print data
        

while True:



    conn, (ip,port) = sever.accept()
    print ("wellcome to "+ip+" connecting server! ! !")
    start_new_thread(clientthread,(conn,)) 

 
conn.close()
sever.close()
