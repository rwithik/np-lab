import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
message = "Hello, Server"

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    message = input("Enter message to send: ")
    clientSock.sendto(message.encode(), (UDP_IP_ADDRESS, UDP_PORT_NO))
