from socket import *
import threading
from types import TracebackType
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)


def handle_cliente(client_socket):
    while True:
        sentence = client_socket.recv(1024).decode()
        capitalizedSentence = sentence.upper()
        client_socket.send(capitalizedSentence.encode())   


print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    x = threading.Thread(target=handle_cliente, args=(connectionSocket,))
    x.start()
    
connectionSocket.close()