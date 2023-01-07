import base64

import cv2
import imutils

from udp.utils.constants import WIDTH, JPEG_QUALITY
from udp.video_func.filters import apply_invert


def create_capture():
    return cv2.VideoCapture(0)

def run_capture(video, server_socket, address: str) -> None:
    while video.isOpened():
        _, frame = video.read()
        # frame = imutils.resize(frame, width=WIDTH)

        inverted = apply_invert(frame)
        inverted = imutils.resize(inverted, width=WIDTH)
        get_send_buffer(inverted, server_socket, address)

        cv2.imshow('SERVER SIDE CAPTURE', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            server_socket.close()
            break

def get_send_buffer(filtered_frame, server_socket, address):
    _, buffer = cv2.imencode('.jpg', filtered_frame, [cv2.IMWRITE_JPEG_QUALITY, JPEG_QUALITY])
    frame_buffer = base64.b64encode(buffer)

    server_socket.sendto(frame_buffer, address)
