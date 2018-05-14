#Logging with NFC
import binascii
import socket
import time
import signal
import sys

import Adafruit_PN532 as PN532



DELAY = 0.5



def connectToNFC():
    def close(signal, frame):
        sys.exit(0)
    # GPIO 18, pin 12
    CS   = 18
    # GPIO 23, pin 16
    MOSI = 23
    # GPIO 24, pin 18
    MISO = 24
    # GPIO 25, pin 22
    SCLK = 25
    
    signal.signal(signal.SIGINT, close)


    pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
    pn532.begin()
    pn532.SAM_configuration()
    return pn532
def logIn(NFC):
     ID = [21695,176682,203231,203277,176784,150035,176999]
     
     while True:
         
         UserId = NFC.read_passive_target()
         
         if UserId is None:
            continue
            
         UserId = format(binascii.hexlify(UserId))
         UserId = int(UserId, 16) // 10000
        
         if UserId in ID:
             print("Zalogowano")
             return True
         else:
             print("Nieuprawniony")
             return False
        