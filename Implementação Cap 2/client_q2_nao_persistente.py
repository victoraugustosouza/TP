from socket import *
serverName = 'localhost'
serverPort = 12000

while True:
    sentence = input('Input lowercase sentence:')
    if sentence=="SAIR":
        break
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    clientSocket.send(sentence.encode())
    print("sent")
    modifiedSentence = clientSocket.recv(1024)
    print('From Server: ', modifiedSentence.decode())
    clientSocket.close()