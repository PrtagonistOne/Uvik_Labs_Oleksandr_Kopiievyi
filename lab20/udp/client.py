import cv2, socket
import base64

from udp.video_func.client_video_func import run_client_capture

server_address_port = ('127.0.0.1', 20001)
buffer_size = 64_000
message = b'Hello'


with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as client_socket:
    client_socket.sendto(message, server_address_port)

    while True:
        try:
            packet,_ = client_socket.recvfrom(buffer_size)
            data = base64.b64decode(packet, ' /')
            run_client_capture(data)
            key = cv2.waitKey(1) & 0xFF

            if key == ord('q'):
                break
        except socket.timeout:
            print('REQUEST TIMED OUT')
            break
        except KeyboardInterrupt:
            print('Client has ended the request')
            break
