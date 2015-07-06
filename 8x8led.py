# Changed from
# https://github.com/adafruit/Adafruit_Python_LED_Backpack\
# /blob/master/examples/matrix8x8_test.py

import time
import Image
import ImageDraw
from Adafruit_LED_Backpack import Matrix8x8

import random
import eightqueen_func as eq

wait_time = 0.2
on_time = 1

display = Matrix8x8.Matrix8x8()
display.begin()

display.clear()
display.write_display()

def on_off(qnum, wtime, flag):
  for num in range(8):
    x, y = qnum[num]
    display.set_pixel(x, y, flag)
    display.write_display()
    time.sleep(wtime)

queen_pattern = eq.get_queens_pattern()

on_off(queen_pattern, wait_time, 1)
time.sleep(on_time)
display.clear()
display.write_display()

display.clear()
display.write_display()
