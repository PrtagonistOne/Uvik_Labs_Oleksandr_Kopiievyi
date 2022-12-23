import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = f"{input('Input the text to encrypt: ').upper()} {input('Input the key: ')}"
    s.sendall(bytes(message, 'ascii'))
    data = s.recv(1024)

print('Received', data)
