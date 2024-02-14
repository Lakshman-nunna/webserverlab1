#import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
# Fill in start
serverHost = '128.238.251.26'
serverPort = 6789
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(5)

# Fill in end
while True:
#establish connection
print('The server is ready to receive')

connectionSocket, addr = serverSocket.accept() # Fill in start             #Fill in end

try:

    message = connectionSocket.recv(4096) # Fill in start             #Fill in end

    filename = message.split()[1]

    f = open(filename[1:])

    outputdata = f.readlines() # Fill in start             #Fill in end

    # send one http header line in to the socket
    # Fill in start

    connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n")
    connectionSocket.send("\r\n")

    # Fill in end

    # Send the content of the requested file to the connection socket
    for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode())
    connectionSocket.send("\r\n".encode())

    connectionSocket.close()

except IOError:
    # Send HTTP response code and message for file not found
    # Fill in start
    connectionSocket.send("HTTP/1.1 404 Not Found\r\n")
    connectionSocket.send("Content-Type: text/html\r\n")
    connectionSocket.send("\r\n")
    connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html><\r\n>")

    # Fill in end
    # Close the client connection socket
    # Fill in start

    serverSocket.close()
    # Fill in end

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
