import socket
import os
import sys

host = "localhost"
port = 5000

s = socket.socket()
print("Connecting to ip:", end = '')
print(host, end = ' ')
print("port:", end = '')
print(port)

s.connect((host, port))
print("Connection successful!")
cur_dir = '~/'
servername = 'dfs@'
separator = '>'

while True:
    print(servername + cur_dir + separator, end='')
    command = str(input().split())
    s.send(command.encode())
    if command == "['exit']":
        break

s.close()

