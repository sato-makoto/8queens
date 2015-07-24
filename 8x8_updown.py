# Changed from
# https://github.com/adafruit/Adafruit_Python_LED_Backpack\
# /blob/master/examples/matrix8x8_test.py

from time import sleep
import all_list as all
import delax_func as de
import eightqueen_func as eq

width = 8
wait_time = 0.1
on_time = 5

queen_pattern, error = eq.main()
print queen_pattern

def updown_and_queens(list):
  for x in list:
     de.line_on_off(x[1], wait_time, 1)
     sleep(0.1)
     de.line_on_off(x[1], wait_time, 0)
     de.dot_on_off(x[1], x[0], 1)

updown_and_queens(queen_pattern)

sleep(3)

eq.display_clear()
