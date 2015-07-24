import random
from time import sleep
import all_list as all
from Adafruit_LED_Backpack import Matrix8x8

width = 8
last = width - 1
display = Matrix8x8.Matrix8x8()
display.begin()

def display_clear():
  display.clear()
  display.write_display()

display_clear()

def on_off(qnum, wtime, flag):
  for num in range(width):
    x, y = qnum[num]
    display.set_pixel(x, y, flag)
    display.write_display()
    sleep(wtime)

def randselect(n):
  random.seed()
  return random.randrange(0,n)

def allclear():
  x, y = 0, 0
  pairs = []
  mylist = all.all_list
  return x, y, pairs, mylist

def ylist(y, a_list):
  tlist = []
  for l in a_list:
     if l[1] == y:
        tlist.append(l)
  return tlist
       
def remove_list(x, y, a_list):
  temp = a_list[:]
  for l in a_list:
    if temp.count(l) and l[0] == x:
      temp.remove(l)
    if temp.count(l) and l[1] == y:
      temp.remove(l)
    if temp.count(l) and (abs(l[0] - x) == abs(l[1] - y)):
      temp.remove(l)
  return temp

def step(y, pairs, next_list, mylist):
  x = next_list[randselect(len(next_list))][0]
  mylist = remove_list(x, y, mylist)
  pairs.append([x, y])
  y+=1
  return  y, pairs, mylist

def main():
  error_time = 0
  x, y, pairs, mylist = allclear()
  while y < width:
    next_list = ylist(y, mylist)
    if len(next_list) > 0:
       y, pairs, mylist = step(y, pairs, next_list, mylist) 
    else:
      error_time += 1
      x, y, pairs, mylist = allclear()
  return pairs, error_time
