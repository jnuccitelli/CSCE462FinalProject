from gpiozero import OutputDevice
from time import sleep
import RPi.GPIO as GPIO
from solver import GetBestMoveFromPhoto
import cv2


GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)
p = GPIO.PWM(18,100)
p.start(0)

IN1 = OutputDevice(14)
IN2 = OutputDevice(15)
IN3 = OutputDevice(18)
IN4 = OutputDevice(23)

step_sequence = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
]

step_sequence_back = [
    [1,0,0,1],
    [0,0,0,1],
    [0,0,1,1],
    [0,0,1,0],
    [0,1,1,0],
    [0,1,0,0],
    [1,1,0,0],
    [1,0,0,0]
]

def set_step(w1,w2,w3,w4):
        IN1.value = w1
        IN2.value = w2
        IN3.value = w3
        IN4.value = w4

def step_motor(steps):
        for _ in range(steps):
                for step in (step_sequence):
                        set_step(*step)
                        sleep(0.01)

def step_motor_back(steps):
        for _ in range(steps):
                for step in (step_sequence_back):
                        set_step(*step)
                        sleep(0.01)

def play_piece():
        p.ChangeDutyCycle(8)
        sleep(2)
        p.ChangeDutyCycle(10.4)
        sleep(2)
        p.ChangeDutyCycle(8)
        sleep(2)

numMoves = 0
startpos = 3


while(True):
    cam_port = -1
    cam = cv2.VideoCapture(cam_port)
    newpos = GetBestMoveFromPhoto(numMoves,cam)[1]
    cam.release()
    print("moving servo")
    while (startpos != newpos):
            if (startpos > newpos):
                    step_motor_back(45)
                    startpos -= 1
            if (startpos < newpos):
                    step_motor(45)
                    startpos += 1

    play_piece()
    step_motor(4)
    sleep(2)
    step_motor_back(8)
    sleep(2)
    step_motor(4)
    numMoves += 1
    print("piece played waiting for opponent")
    sleep(10)
    numMoves += 1
    print("starting next move")


