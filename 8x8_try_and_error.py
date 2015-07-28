#!/usr/bin/env python
from time import sleep
import eightqueen_func as eq
import delax_func as de

width = 8
wait_time = 0.4
sleeptime = 5
repeat_time = 3
oklist = [ [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], 
           [1, 2],                         [1, 6], 
           [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], 

           [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], 
                           [5, 4], 
                   [6, 3],         [6, 5],   
           [7, 2],                         [7, 6]] 
nolist = [ [0, 2], [0, 3], [0, 4], [0, 5], 
                   [1, 3],                         
                           [2, 4],
           [3, 2], [3, 3], [3, 4], [3, 5],

                   [5, 3], [5, 4], [5, 5],
                   [6, 3],         [6, 5],   
                   [7, 3], [7, 4], [7, 5]]

def ok_no_on_off(list):
  for x in range(3):
    de.ok_on(list, 1)
    sleep(wait_time)
    de.ok_on(list, 0)
    sleep(wait_time)

def try_and_error_main():
  eq.display_clear()
  error_time = 0
  x, y, pairs, mylist = eq.allclear()
  while y < width:
    next_list = eq.ylist(y, mylist)
    if len(next_list) > 0:
       y, pairs, mylist = eq.step(y, pairs, next_list, mylist)
       eq.display.set_pixel(pairs[-1][0], pairs[-1][1], 1)
       eq.display.write_display()
       sleep(0.1)
    else:
      sleep(sleeptime)
      ok_no_on_off(nolist)
      error_time += 1
      x, y, pairs, mylist = eq.allclear()
      eq.display_clear()
  sleep(sleeptime)
  ok_no_on_off(oklist)
  return pairs, error_time

pairs, error_time = try_and_error_main()
print '{} times fault!'.format(error_time)

de.on(pairs)
sleep(sleeptime)

eq.display_clear()
