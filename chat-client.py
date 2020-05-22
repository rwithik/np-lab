#!/bin/python

import socket
import select
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.connect(("127.0.0.1", 8888))
print("Connected!")

while True:
    read, write, error = select.select([sys.stdin, sock], [], [])
    print(read)
    for r in read:
        # print(r)
        if r == sock:
            msg = sock.recv(2048)
            print(msg.decode())
        else:
            msg = sys.stdin.readline()
            sock.send(msg.encode())
            # sys.stdout.write("You >> ")
            # sys.stdout.write(msg)
            # sys.stdout.flush()
sock.close()
