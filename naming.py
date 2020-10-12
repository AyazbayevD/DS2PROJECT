import socket
import os
import threading
import random
from time import sleep

abs_path = "C:\\Users\\danat\\PyCharmProjects\\DS_PROJECT_2\\"

hosts = []
ports = []
clients = []

f = open(abs_path + "hosts.txt", "r").readlines()
for line in f:
    hosts.append(line.strip())
f = open(abs_path + "ports.txt", "r").readlines()
for line in f:
    ports.append(int(line.strip()))
f = open(abs_path + "clients.txt", "r").readlines()
for line in f:
    clients.append(line.strip())

def conn(sock, client_addr):

    if client_addr[0] not in clients:
        # adding new client to the list of clients
        f = open(abs_path + "clients.txt", "a")
        f.write(client_addr[0] + "\n")
        f.close()

        # choosing random server from available ones
        id = random.randint(0, len(hosts) - 1)
        server_addr = hosts[id]
        server_port = ports[id]

        # connecting to the file server
        new_sock = socket.socket()
        print("Connecting to ip:", end='')
        print(server_addr, end=' ')
        print("port:", end='')
        print(server_port)
        new_sock.connect((host, port))
        print("Connection successful!")

        # saying server to create new directory for the new client
        new_sock.send(("new_client " + client_addr[0]).encode())


    data = ''
    cur_dir = '~/'
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

        # if no commands passed, we proceed to receive next commands
        # -------------------------------------------------------------------
        if len(command) == 0:
            continue
        # -------------------------------------------------------------------

        # if exit command passed, we break connection with client
        # -------------------------------------------------------------------
        if command[0] == "exit":
            break
        # -------------------------------------------------------------------

        # initialize root directory
        # -------------------------------------------------------------------
        if command[0] == "init":
            break
        # -------------------------------------------------------------------



    sock.close()
    print("User with ip:", end='')
    print(addr, end=' ')
    print("has disconnected")

host = ""
port = 5000
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

