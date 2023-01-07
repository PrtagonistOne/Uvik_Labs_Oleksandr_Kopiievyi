import cv2


def apply_invert(frame):
    return cv2.bitwise_not(frame)
