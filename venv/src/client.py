import socket
import threading

HOST, PORT = 'localhost' ,8080
name = input('type your name: ')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.send(name)

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

sock.connect((HOST, PORT))
# send_thread = threading.Thread(target=send, daemon=True)
# receive_thread = threading.Thread(target=receive, daemon=True)
# send_thread.start()
# receive_thread.start()
while True:
    data = input(name + ': ')
    sock.sendall(bytes(name + ": " + data, 'utf-8'))
    response = sock.recv(1024)
    print(response.decode('utf-8'))
sock.close()

