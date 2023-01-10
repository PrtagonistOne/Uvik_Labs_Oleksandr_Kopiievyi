import socket

from tcp.utils.constants import HOST, PORT
from _thread import *

def client_handler(connection):
    with connection:
        while True:
            try:
                data = connection.recv(2048)
            except ConnectionResetError:
                print('Connection broken by the user.')
                break
            message = data.decode('utf-8')
            if message == '/q':
                break
            print(message)
            reply = f'{message}'
            connection.sendall(str.encode(reply))

def accept_connections(ServerSocket):
    Client, address = ServerSocket.accept()
    print(f"Connected by {address}")
    start_new_thread(client_handler, (Client, ))

def start_server():
    print('Type "/q" to leave the chat.')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((HOST, PORT))
        except socket.error as e:
            print(e)
        s.listen()

        while True:
            accept_connections(ServerSocket=s)


if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print('TCP server down')
