#Logging with NFC
import binascii
import socket
import time
import signal
import sys
import LCD
from DatabaseModule import Database

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
     mylcd = LCD.lcd()
     database = Database()
     while True:
         
         
         UserId = NFC.read_passive_target()
         if UserId is None:
             mylcd.lcd_clear()
             mylcd.lcd_display_string("Przyloz karte",1)
             mylcd.lcd_display_string("aby zaglosowac",2)
    
             
         if UserId is None:
             continue
          
         UserId = format(binascii.hexlify(UserId))
         UserId = str(int(UserId, 16))
         isAllowed = database.isAllowedToVote(UserId)
         if isAllowed == 1 :
             if UserId =='2169576700':
                 mylcd.lcd_clear()
                 mylcd.lcd_display_string("Administracja",1)
                 time.sleep(3)
                 mylcd.lcd_clear()
                 mylcd.lcd_display_string("Nieb=START",1)
                 mylcd.lcd_display_string("Czer=STOP,3=Arch",2)
                
             else:
                 if database.ifopen()==False:
                     mylcd.lcd_clear()
                     mylcd.lcd_display_string("Brak otwartego ",1)
                     mylcd.lcd_display_string("glosowania.",2)
                     time.sleep(3)
                     continue
                 mylcd.lcd_clear()
                 mylcd.lcd_display_string("Zalogowano",1)
                 time.sleep(3)
                
                 mylcd.lcd_clear()
                 mylcd.lcd_display_string("Tak czy nie ?",1)
                 mylcd.lcd_display_string("Dokonaj wyboru",2)
             return (True, UserId)
         elif isAllowed == 0:
             if UserId =='2169576700':
                 mylcd.lcd_clear()
                 mylcd.lcd_display_string("Administracja",1)
                 time.sleep(3)
                 mylcd.lcd_clear()
                 mylcd.lcd_display_string("Nieb=START",1)
                 mylcd.lcd_display_string("Czer=STOP,3=Arch",2)
             if database.ifopen()==False:
                     mylcd.lcd_clear()
                     mylcd.lcd_display_string("Brak otwartego ",1)
                     mylcd.lcd_display_string("glosowania.",2)
                     time.sleep(3)
                     continue
             mylcd.lcd_clear()
             mylcd.lcd_display_string("Nieuprawniony",1)
             mylcd.lcd_display_string("uzytkownik",2)
             time.sleep(2)
             return (False, UserId)
         elif isAllowed == -1:
             mylcd.lcd_clear()
             mylcd.lcd_display_string("Taki uzytkownik",1)
             mylcd.lcd_display_string("nie istnieje",2)
             time.sleep(2)
             return (False, UserId)
         
             
             
        