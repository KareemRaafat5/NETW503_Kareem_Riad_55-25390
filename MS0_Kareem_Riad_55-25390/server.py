import socket
import select
import sys
#initiate server socket with the TCP connection
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# binding the server socket with the localhost as ip and port number
port=5622
server_socket.bind(('192.168.1.2',port)) # '127.0.0.1' is the localhost in ipv4␣↪format
# make the socket listen on this port
server_socket.listen(5)
# listening forever
while True :
    client,add = server_socket.accept() # when a connection to a client is␣↪accepted
    print(">>Connection Established")
  # client.send(bytes("You are connected successfully","utf-8"))
# open a conitional conection --> break the connection when 'CLOSE SOCKET' is␣↪recieved
   #Check if the message was 'CLOSE SOCKET' to close connection
    while True:
    # recieve meassage as bytes 
        msg=client.recv(1024)
    # decoding the bytes into characters
        rmsg=(msg.decode())
    #Check if the message was 'CLOSE SOCKET' to close connection
        if (rmsg=="CLOSE SOCKET"):
            client.close()
            print(">>Connection lost")
            break
        else:
    # otherwise capitalize the decoded message
    # send the response as bytes again
             client.send(bytes(rmsg.upper(),"utf-8"))
        
