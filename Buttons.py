#Buttons
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def Choice():
    while True:
        input_Yes = GPIO.input(21)
        input_No = GPIO.input(20)
        archive = GPIO.input(16)
        if input_Yes == True:
            return 1
        if input_No == True:
            return 0
        if archive = True:
            return 2
        
def AdminChoice():
    while True:
        start = GPIO.input(21)
        close = GPIO.input(20)
        archive = GPIO.input(16)
        if start == True:
            return 1
        if close == True:
            return 0
        if archive = True:
            return 2