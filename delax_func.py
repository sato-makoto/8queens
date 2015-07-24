import random
from time import sleep
from Adafruit_LED_Backpack import Matrix8x8
import all_list as all
display = Matrix8x8.Matrix8x8()
display.begin()
width = 8

def dot_on_off(x, y, flag):
  display.set_pixel(x, y, flag)
  display.write_display()

def on(list):
  display.clear()
  for num in list:
    display.set_pixel(num[0], num[1], 1)
  display.write_display()

def neg_on(list):
  display.clear()
  for w in all.all_list:
    display.set_pixel(w[0], w[1], 1)
  for z in list:
    display.set_pixel(z[0], z[1], 0)
  display.write_display()

def line_on_off(x, wait, flag):
  if flag:
    for y in range(width):
      dot_on_off(x, y, 1)
      sleep(wait)
      dot_on_off(x, y, 0)
  else:
    for y in range(width)[::-1]:
      dot_on_off(x, y, 1)
      sleep(wait)
      dot_on_off(x, y, 0)
