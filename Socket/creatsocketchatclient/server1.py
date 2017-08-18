
import socket 
from thread import *
import re
 

host = '0.0.0.0' 
port = 2004 


sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sever.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

sever.bind((host, port))
hihi=['waiting for messenger! ! !']
huhu=['waiting for messenger! ! !']
i=[1]
u=[1]

sever.listen(5) 
print("waiting for connecting ! ! !. . . . .")
 
def clientthread(conn):
	
	 
	while True:


		data = conn.recv(1024) 
		         
		print data
		da=re.findall(r'Client A',data)
		if da==['Client A']:
			
			huhu.append(data)
			conn.send(hihi[-1])
			
		else:
			n=n+1
			hihi.append(data)
			conn.send(huhu[u[-1]])
	         	


         	

while True:



    conn, (ip,port) = sever.accept()
    print ("wellcome to "+ip+" connecting server! ! !")
    start_new_thread(clientthread,(conn,)) 


 
conn.close()
sever.close()
