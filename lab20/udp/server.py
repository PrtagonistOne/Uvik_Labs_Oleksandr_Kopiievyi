import socket

from udp.video_func.server_video_func import run_capture, create_capture

local_IP = '127.0.0.1'
local_port = 20001
buffer_size = 16_000


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((local_IP, local_port))
    print(f'UDP server up and listening on {local_IP}:{local_port}')

    video_capture = create_capture()
    while True:
        try:
            message, address = server_socket.recvfrom(buffer_size)
            client_IP = f'Client IP Address: {address}'

            run_capture(video=video_capture, server_socket=server_socket, address=address)

        except KeyboardInterrupt:
            print('UDP Server down')
            break
    print('UDP Server down Socket connection closed')
