# Import socket module
from socket import * 
import sys # In order to terminate the program

serverName = 'localhost'
# Assign a port number
serverPort = 1234

# Bind the socket to server address and server port
clientSocket = socket(AF_INET, SOCK_STREAM)

#connect to server
clientSocket.connect((serverName, serverPort))

#Recive the Client name
modifiedSentence = clientSocket.recv(1024)
print('From server: ', modifiedSentence.decode())

#user input loop
sentence= ""
while sentence != "exit":

    sentence = input(' Input message: ')
       
    clientSocket. send(sentence.encode())

    #close connection
    if sentence == "exit":
        clientSocket.close() 
        exit

    #Connection not closed, continue operation
    else:
        modifiedSentence = clientSocket.recv(1024)

        print('From server: ', modifiedSentence.decode())
