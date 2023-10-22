import socket
#initiate Client socket with the TCP connection
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# binding the client socket with the localhost as ip and port number
port=5634
# try to connect to the server with associated port and id
client_socket.connect(('127.0.0.1',port)) #'127.0.0.1' is the localhost in ipv4␣↪format
# open a connection until sending CLOSE SOCKET
#msg=client_socket.recv(1024)
print(">>Connection established")
while True:
    message=input("Enter your message:" )
# send message as bytes
    client_socket.send(bytes(message,"utf-8"))
    if (message=="CLOSE SOCKET"):
        print(">>socket closed")
        client_socket.close()
        break
    
#recieve respose if exists
    server_reply=client_socket.recv(1024)
    print("Server response:"+ server_reply.decode())