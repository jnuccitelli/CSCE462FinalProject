import cv2
from camera import CaptureBoard
cam_port = 0
cam = cv2.VideoCapture(cam_port)

CaptureBoard(cam)

