import socket

server_address_port = ('127.0.0.1', 20001)
buffer_size = 1024

# Створюємо UDP socket клієнта
UDP_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


while True:
    msg_from_client = input('Your message to the world - ')
    bytes_to_send = str.encode(msg_from_client)
    # Відправка до сервера через створенний сокет
    UDP_client_socket.sendto(bytes_to_send, server_address_port)

    smg_from_server = UDP_client_socket.recvfrom(buffer_size)

    msg = f'Message from Server {smg_from_server[0]}'
    print(msg)
