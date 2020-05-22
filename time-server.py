#!/bin/python

import socket
import time

ip = "127.0.0.1"
port = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((ip, port))

while True:
    req, client_ip = sock.recvfrom(10)
    print(f"Time request from {client_ip}")

    sock.sendto(str.encode(time.asctime()), client_ip)
