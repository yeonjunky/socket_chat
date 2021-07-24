import socket
import threading
import sys


CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K'
HOST, PORT = 'localhost' ,8080

def delete_last_line(n=1):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)

# name = input('type your name: ')
name = 'jun'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))

data = sock.recv(1024)
try:
    while True:
        data = input(name + ': ')
        sock.sendall(bytes(name + ": " + data, 'utf-8'))
        delete_last_line()
        response = sock.recv(1024)
        print(response.decode('utf-8'))
except KeyboardInterrupt:
    sock.close()

sys.exit()
