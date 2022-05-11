from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
N = 250
contador = 0
while True:
    sentence = str(contador)+" "
    if contador==N:
        break
    clientSocket.send(sentence.encode())
    contador = contador + 1
clientSocket.close()