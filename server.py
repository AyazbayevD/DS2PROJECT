import socket
import os
import threading


def conn(sock, client_addr):
    data = ''
    cur_dir ='~/'
    while True:
        chunk = sock.recv(4096).decode()
        if not chunk:
            break

        # parsing command from the received information from socket
        # -------------------------------------------------------------------
        command = []
        part = ''
        opened = False
        for i in chunk:
            if i == "'":
                if opened:
                    command.append(part)
                    part = ''
                opened = not opened
                continue
            if opened:
                part += i
        # -------------------------------------------------------------------

        # if exit command passed, we break connection with client
        # -------------------------------------------------------------------
        if command[0] == "exit":
            break
        # -------------------------------------------------------------------

    print(data)
    sock.close()
    print("User with ip:", end='')
    print(addr, end=' ')
    print("has disconnected")

host = ""
port = 5050
s = socket.socket()
s.bind((host, port))
s.listen(5)
print("Listening at ip:", end = '')
print(host, end = ' ')
print("port:", end = '')
print(port)

while True:
    sock, addr = s.accept()
    print("User with ip:", end='')
    print(addr, end=' ')
    print("has connected")
    thread = threading.Thread(target=conn, args=(sock, addr,))
    thread.start()

