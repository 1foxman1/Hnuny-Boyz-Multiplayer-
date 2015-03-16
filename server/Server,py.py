import socket
import thread

BUFFER_SIZE=1024
TCP_IP= socket.gethostbyname(socket.gethostname())
TCP_PORT=3456
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
