#Voting
import LoggingModule
import Buttons
import time
import LCD
from DatabaseModule import Database
from VotingAdministrator import Administrator

mylcd = LCD.lcd()
NFC_Reader = LoggingModule.connectToNFC()
database = Database()
admin = Administrator()

while True:
    
    Allowed = LoggingModule.logIn(NFC_Reader)
    if Allowed[1] == "2169576700":   
        while True:
            if Buttons.AdminChoice() ==2:
                admin.Archive()
                break
            if Buttons.AdminChoice() == 1:
                admin.closeVoting()
                admin.setVotedToNo()
                admin.startPoll()
                break
            if Buttons.AdminChoice() == 0:
                admin.closeVoting()
                break
    else:
        while Allowed[0]:
            if Buttons.Choice() == 1:
                
                database.addYesVote()
                database.setVotedToYes(Allowed[1])
                mylcd.lcd_display_string("Zaglosowano",1)
                break
            if Buttons.Choice() == 0:
                database.addNoVote()
                database.setVotedToYes(Allowed[1])
                mylcd.lcd_display_string("Zaglosowano",1)
                break
    for t in range(5,0,-1):
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Poczekaj {} sek.".format(t),1)
        time.sleep(1)

mylcd.lcd_display_string("Nieuprawniony uzytkownik",1)