import socket

local_IP = '127.0.0.1'
local_port = 20001
buffer_size = 1024

msg_from_server = 'Hello UDP Client!'
bytes_to_send = str.encode(msg_from_server)

# Створюємо датаграм сокэт
UDP_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Прив'язка до адресу та порту
UDP_server_socket.bind((local_IP, local_port))

print(f'UDP server up and listening on {local_IP}:{local_port}')

while True:
    message, address = UDP_server_socket.recvfrom(buffer_size)
    client_msg = f'Message from Client: {message}'
    client_IP = f'Client IP Address: {address}'

    print(client_msg)
    print(client_IP)

    # Відправка відповіді клієнту
    UDP_server_socket.sendto(bytes_to_send, address)
