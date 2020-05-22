#!/bin/python

import socket
import threading


class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr

    def run(self):
        conn.send("Welcome to this chatroom.")
        while True:
            try:
                msg = conn.recv(1024)
                if msg:
                    print(f"{addr}: {msg}")
                    broadcast(f"{addr}: {msg}", conn)
                else:
                    remove(conn)
            except:
                continue


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(("127.0.0.1", 8888))

sock.listen(100)

clients = []


def client_fn(conn, addr):
    conn.send("Welcome to this chatroom.")
    while True:
        try:
            msg = conn.recv(1024)
            if msg:
                print(f"{addr}: {msg}")
                broadcast(f"{addr}: {msg}", conn)
            else:
                remove(conn)
        except:
            continue


def broadcast(msg, conn):
    for client in clients:
        if client != conn:
            try:
                client.send(msg)
            except:
                client.close()
                remove(client)


def remove(conn):
    if conn in clients:
        clients.remove(conn)


print("Waiting for connections...")
while True:
    conn, addr = sock.accept()
    clients.append(conn)
    print(addr, "connected")
    # thread.start_new_thread(client_fn, (conn, addr))
    thread = ClientThread(conn, addr)
    thread.start()
