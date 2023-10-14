# Python program to implement server side of chat room.
import socket
import select
import sys
#initiate Client socket with the TCP connection
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# binding the client socket with the localhost as ip and port number
port=5622
# try to connect to the server with associated port and id
client_socket.connect(('192.168.1.2',port)) #'127.0.0.1' is the localhost in ipv4␣↪format
# open a connection until sending CLOSE SOCKET
#msg=client_socket.recv(1024)
print(">>Connection established")
while True:
    message=input("Enter your message:" )
# send message as bytes
    client_socket.send(bytes(message,"utf-8"))
    if (message=="CLOSE SOCKET"):
        print(">>socket closed")
        break
    
#recieve respose if exists
    reply=client_socket.recv(1024)
    print(reply.decode())