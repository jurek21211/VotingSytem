import LCD

from time import *

mylcd = LCD.lcd()
mylcd.lcd_clear()
mylcd.lcd_display_string("Hello World!",1)
sleep(20)