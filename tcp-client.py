import socket

HOST = "127.0.0.1"
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = input("Enter message to send: ")
        s.sendall(msg.encode())
        data = s.recv(1024)

        print("Received", repr(data))
