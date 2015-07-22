# Changed from
# https://github.com/adafruit/Adafruit_Python_LED_Backpack\
# /blob/master/examples/matrix8x8_test.py

from time import sleep
import eightqueen_func as eq

wait_time = 0.2
on_time = 5

#eq.display_clear()
queen_pattern, error = eq.main()
print '{} times error!'.format(error)

eq.on_off(queen_pattern, wait_time, 1)
sleep(on_time)
eq.display_clear()
