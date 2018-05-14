#Voting
import LoggingModule
import Buttons
import time

NFC_Reader = LoggingModule.connectToNFC()

 #True / False
voted = False
while True:
    print("Przyloz karte aby sie zalogowac: ")
    Allowed = LoggingModule.logIn(NFC_Reader)
    while Allowed:
        if Buttons.Choice(voted) == 1:
            print("tak")
            break
        if Buttons.Choice(voted) == 0:
            # vote no
            pass
    for t in range(5,0,-1):
        print("Poczekaj jeszcze: {} sek.".format(t))
        time.sleep(1)

print("Nieuprawniony do glosowania")