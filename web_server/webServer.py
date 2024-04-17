#import socket module 
from socket import * 
import sys # In order to terminate the program 
 
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 50000
serverSocket.bind(("localhost", serverPort)) # this lets the server work on the actual host IP address
serverSocket.listen()
while True: 
    #Establish the connection 
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try: 
        message = connectionSocket.recv(2048)
        print("message =", message)
        if ' ' not in str(message):
            continue
        filename = message.split()[1]
        print("filename = " + str(filename))
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)):            
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send('\r\n'.encode())
        connectionSocket.close() 
    except IOError:
        #Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        outputdata = open('404.html').read()
        for i in range(0, len(outputdata)): # sends the 404 not found page
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send('\r\n'.encode())
        #Close client socket 
        connectionSocket.close()