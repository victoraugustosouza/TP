from socket import *
import threading

def handle_cliente(message,send_socket,clientAddress):
    modifiedMessage = message.decode().upper()
    with lock:      
        send_socket.sendto(modifiedMessage.encode(), clientAddress)


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

send_socket =  socket(AF_INET, SOCK_DGRAM)
lock = threading.Lock()
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    x = threading.Thread(target=handle_cliente, args=(message, send_socket,clientAddress))
    x.start()


    