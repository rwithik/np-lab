import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 9999))

    fileName = input("File name: ")
    # fileName = "test-file.txt"

    outputFile = open("received.txt", "wb")
    s.send(fileName.encode())
    pid = s.recv(1024)
    print(f"PID of server process: {pid.decode()}")
    data = s.recv(1024)
    while data:
        if not data.decode():
            s.shutdown(socket.SHUT_WR)
            break
        # print(data)
        outputFile.write(data)
        data = s.recv(1024)

    s.close()
    print(f"{fileName} received.")


if __name__ == "__main__":
    main()
