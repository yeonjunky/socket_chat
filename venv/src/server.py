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
        print(data)
        reply = 'Server Says: ' + data.decode('utf-8')
        
        if not data:
            break
        client.sendall(str.encode(reply))
    client.close()

def serve_data(clients, data, sent_client):
    for client in clients:
        if client != sent_client:
            client.send(data)

def command(server):
    com = input()
    if com == 'q':
        server.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen(MAX_CLIENTS)

while True:
    client, addr = server.accept()
    print('connected by', addr)
    threading.Thread(target=threaded_client, args=(client,)).start()
    threading.Thread(target=command, args=(server, )).start()

