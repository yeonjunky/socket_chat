import socket
import threading
import sys


HOST, PORT = 'localhost', 8080
MAX_CLIENTS = 5

clients = []
msg = ""


def command(server):
    com = input()
    if com == 'q':
        server.close()

def add_client_thread(server):
    client, addr = server.accept()
    print('connected by', addr)
    clients.append(client)
    threading.Thread(target=client_thread, args=(client, )).start()

def client_thread(client):
    client.send("Welcome to server!".encode('utf-8'))
    while True:
        data = client.recv(1024)
        print(data.decode('utf-8'))
        if not data:
            break
        msg = data.decode('utf-8')
        send_to_all_clients(msg, clients)

    client.close()

def send_to_all_clients(msg, clients):
    encoded_msg = msg.encode('utf-8')
    for client in clients:
        client.send(encoded_msg)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
print("Waiting for connect")
server.listen(MAX_CLIENTS)

try:
    while True:
        add_client_thread(server)
except KeyboardInterrupt:
    server.close()
sys.exit()
