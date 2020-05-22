import socket
from _thread import start_new_thread
import threading
from os import getpid

print_lock = threading.Lock()
pid = getpid()


def threaded(c):
    while True:
        try:
            data = c.recv(1024)
        except Exception:
            break

        if not data:
            break

        fileName = data.decode()
        print(f"filename: {fileName}")
        c.send(str(pid).encode())

        try:
            file = open(fileName, "rb")
        except FileNotFoundError:
            c.send("File Not Found")
            print("File Not Found")
            break

        inp = file.read(1024)
        while inp:
            c.send(inp)
            inp = file.read(1024)
        c.send("".encode())

        c.close()

    print(f"{c} disconnected")
    print_lock.release()


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 9999))
    s.listen(5)
    print("Listening for connections")

    while True:

        c, addr = s.accept()

        print_lock.acquire()
        print("Connected to :", addr)

        start_new_thread(threaded, (c,))
    s.close()


if __name__ == "__main__":
    main()
