import socket
import threading
import sys
from _thread import start_new_thread


HOST, PORT = 'localhost', 8080
MAX_CLIENTS = 5

def threaded_client(client):
    client.send(str.encode("Welcome to server!"))
    while True:
        data = client.recv(1024)
        reply = 'Server Says: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen(MAX_CLIENTS)

while True:
    client, addr = server.accept()
    print('connected by', addr)
    threading.Thread(target=threaded_client, args=(client,))
server.close()

# try:
#     while True:
#         client, addr = server.accept()
#         threading.Thread(target=threaded_client, args=(client,))
#
# except KeyboardInterrupt:
#     socket.close()

# def send_msg():
#     while True:

def serve_data(clients, data, sent_client):
    for client in clients:
        if client != sent_client:
            client.send(data)

