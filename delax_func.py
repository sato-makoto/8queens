import random
from time import sleep
import eightqueen_func as eq
from Adafruit_LED_Backpack import Matrix8x8
display = Matrix8x8.Matrix8x8()
display.begin()

def on(list):
  display.clear()
  for num in list:
    display.set_pixel(num[0], num[1], 1)
  display.write_display()

def neg_on(list):
  display.clear()
  all_list = [[x, y] for x in range(8) 
     for y in range(8)]
  for w in all_list:
    display.set_pixel(w[0], w[1], 1)
  for z in list:
    display.set_pixel(z[0], z[1], 0)
  display.write_display()
