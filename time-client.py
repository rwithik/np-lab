#!/bin/python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(str.encode("Time request"), ("127.0.0.1", 8888))

reply = sock.recvfrom(1024)

print(f"Reply from time server: {reply[0].decode()}")
