import socket
import threading
port = 8008
addr = ('192.168.43.230', port)
Lock = threading.Lock()
threads = []  # List to store the active threads
def threaded(client, addr):
     print("[NEW CONNECTION] " + str(addr) + " connected.")
     while True :
         # Functionality of the server
         # recieve meassage as bytes 
         msg=client.recv(1024)
          # decoding the bytes into characters
         rmsg=(msg.decode())
          #Check if the message was 'CLOSE SOCKET' to close connection
         if (rmsg=="CLOSE SOCKET"):
             print( str(addr) + " lost connection.")
             #Lock.release()
             break
         else:
          # otherwise capitalize the decoded message
          # send the response as bytes again
              print(rmsg)
         # do not forget to release the thread if you've locked it
   
     client.close()
     threads.remove(threading.current_thread())
     print(f"[ACTIVE CONNECTIONS] {len(threads)}")
     
     
     
def main():
     global threads
     print(" Server is starting...")
     # Open server socket as in MS0
     #initiate server socket with the TCP connection
     server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     # binding the server socket with the localhost as ip and port number
     server_socket.bind(('192.168.43.230',port)) # '127.0.0.1' is the localhost in ipv4 format
     # make the socket listen on this port
     server_socket.listen(5)
     #
     #
     while True:
         client, addr = server_socket.accept()
         # Locking the thread that will be assigned to the client
         # start new thread
         #Lock.acquire()
         ##(threading.Thread(threaded(client, addr))).start()
         
         thread= threading.Thread(target=threaded, args=(client, addr))
         threads.append(thread)
         thread.start()
        ## Lock.release()
         ##print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        # print(f"[ACTIVE CONNECTIONS] {len(threads)}")
          # Remove completed threads from the list
         #threads = [t for t in threads if t.is_alive()]
         print(f"[ACTIVE CONNECTIONS] {len(threads)}")
         
if __name__ == "__main__":
    main()
