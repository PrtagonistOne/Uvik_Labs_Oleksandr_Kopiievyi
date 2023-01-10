import cv2
import numpy as np

def run_client_capture(data):
    npdata = np.fromstring(data, dtype=np.uint8)
    frame = cv2.imdecode(npdata, 1)

    cv2.imshow("CLIENT SIDE CAPTURE", frame)
