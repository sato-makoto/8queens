import random
from time import sleep
# import eightqueen_func as eq
from Adafruit_LED_Backpack import Matrix8x8

display = Matrix8x8.Matrix8x8()
display.begin()

def on(list):
  display.clear()
  for num in list:
    display.set_pixel(num[0], num[1], 1)
  display.write_display()
