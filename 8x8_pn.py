# Changed from
# https://github.com/adafruit/Adafruit_Python_LED_Backpack\
# /blob/master/examples/matrix8x8_test.py

from time import sleep
import eightqueen_func as eq
import delax_func as de

queen_pattern, error = eq.main()
for x in range(10):
 de.on(queen_pattern)
 sleep(0.7)
 de.neg_on(queen_pattern)
 sleep(0.3)

eq.display_clear()
