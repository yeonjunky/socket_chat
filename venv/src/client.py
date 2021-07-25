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

def receive(sock):
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))

def send_msg(sock):
    while True:
        msg = input(name + ': ')
        delete_last_line()
        sock.send(msg.encode('utf-8'))

name = input('type your name: ')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))

data = sock.recv(1024)
try:
    while True:
        threading.Thread(target=receive, args=(sock, )).start()
        msg = name + ': ' + input()
        delete_last_line()
        sock.send(msg.encode('utf-8'))
except KeyboardInterrupt:
    sock.close()

sys.exit()
