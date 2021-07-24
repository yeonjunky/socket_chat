import socket
import threading

HOST, PORT = 'localhost' ,8080
# name = input('type your name: ')
name = 'jun'

def send():
    while True:
        data = input(name + ': ')
        sock.sendall(bytes(name + ": " + data, 'utf-8'))
    sock.close()

def receive():
    while True:
        data = str(sock.recv(1024), 'utf-8')
        print(data)
    sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))

data = sock.recv(1024)

while True:
    data = input(name + ': ')
    sock.sendall(bytes(name + ": " + data, 'utf-8'))
    response = sock.recv(1024)
    print(response.decode('utf-8'))

sock.close()
