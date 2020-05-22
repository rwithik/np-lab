import socket

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind(("127.0.0.1", 6789))

while True:
    data, addr = serverSock.recvfrom(1024)
    print("Message:", data)
