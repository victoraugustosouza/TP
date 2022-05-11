from email import message
from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
inicio = clientSocket.recv(1024)
print(inicio.decode())
login = input()
clientSocket.send(login.encode())
inicio = clientSocket.recv(1024)
print(inicio.decode())
senha = input()
clientSocket.send(senha.encode())
inicio = clientSocket.recv(1024)
print(inicio.decode())
clientSocket.close()