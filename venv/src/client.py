import socket
import threading
import sys


CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K'
HOST, PORT = 'localhost', 8080
thread_status = True # true: on, false: off

def delete_last_line(n=1):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)

def receive(sock, thread_status):
    while thread_status:
        data = sock.recv(1024)
        print(data.decode('utf-8'))


name = input('type your name: ')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))

data = sock.recv(1024)

try:
    threading.Thread(target=receive, args=(sock, thread_status)).start()
    while True:
        msg = name + ': ' + input()
        if msg[len(name)+2:] == "!disconnect":
            thread_status = False
            break
        else:
            delete_last_line()
            sock.send(msg.encode('utf-8'))

except KeyboardInterrupt:
    sock.close()

sock.close()
sys.exit()
