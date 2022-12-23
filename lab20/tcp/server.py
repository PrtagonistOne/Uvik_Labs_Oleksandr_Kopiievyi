import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 65432)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

sock.listen(1)


def encrypt(text, s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

    return result


while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        # Receive the data in small chunks and retransmit it
        while data := connection.recv(1024):
            print(f'received {data}')
            message, key = data.split()
            encrypted_message = encrypt(str(message), int(key))

            bytes_to_send = str.encode(encrypted_message)
            print('sending data back to the client')
            connection.sendall(bytes_to_send)
    finally:
        connection.close()
