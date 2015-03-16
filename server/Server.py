import socket
import thread

BUFFER_SIZE=1024
TCP_IP= "25.86.198.77"
TCP_PORT=3334
data="NO_DATA"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Server Working"
    
s.bind((TCP_IP,TCP_PORT))
s.listen(3)

conn1, addr2 = s.accept()
print "Player 1 connected"


conn2, addr2 = s.accept()
print "Player 2 connected"

      
def main():
    try:
        thread.start_new_thread( recieve, (conn1, 1))
    except:
        print "Player 1 failed to start!"
        

    try:
        thread.start_new_thread( recieve, (conn2, 2))
    except:
        print "Player 2 failed to start!"
    

    
def recieve (conn, player):
    print "player %d started playing"%(player)
    data = "no data"
    
    while data != "exit":
        data = conn.recv(BUFFER_SIZE)
        print data

        if(player == 1):
            conn2.send(data)
        else:
            conn1.send(data)
        
    conn.close()  

if __name__ == "__main__":
  main()
