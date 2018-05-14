#Buttons
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def Choice(voted):
    while True:
        input_Yes = GPIO.input(21)
        input_No = GPIO.input(20)
        if input_Yes == True and voted == False:
            voted = True
            return 1
        if input_No == True and voted == False:
            voted = True
            return 0
    