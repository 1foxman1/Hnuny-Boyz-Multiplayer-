import socket
import thread

BUFFER_SIZE=1024
TCP_IP= "25.164.130.160"
TCP_PORT=3334
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Server Working"
s.bind((TCP_IP,TCP_PORT))
s.listen(3)
data="NO_DATA"
msg="NONE"
conn, addr = s.accept()
print "Connection Address:" , addr
while data != "exit":
    data = conn.recv(BUFFER_SIZE)
    print data
conn.close()
