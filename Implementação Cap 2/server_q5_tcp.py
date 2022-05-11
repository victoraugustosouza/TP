from socket import *
import threading
from types import TracebackType
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)


def handle_cliente(client_socket):
    while True:
        mensagem =  "Digite Login:"
        client_socket.send(mensagem.encode())
        login = client_socket.recv(1024).decode()   
        mensagem =  "Digite Senha:"
        client_socket.send(mensagem.encode())
        senha = client_socket.recv(1024).decode()
        if login=="admin" and senha=="123":
            mensagem = "Você está Logado"
            client_socket.send(mensagem.encode())
        else:
            mensagem = "Erro: login ou senha errado"
            client_socket.send(mensagem.encode())           


    client_socket.close()


print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    x = threading.Thread(target=handle_cliente, args=(connectionSocket,))
    x.start()
    
connectionSocket.close()