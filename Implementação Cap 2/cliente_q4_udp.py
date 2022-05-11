from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
N = 25
contador = 0
while True:
    sentence = str(contador)+" "
    if contador==N:
        break
    clientSocket.sendto(sentence.encode(),(serverName, serverPort))
    contador = contador + 1
clientSocket.close()



