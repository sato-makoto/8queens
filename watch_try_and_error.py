#!/usr/bin/env python
import random
from time import sleep
import eightqueen_func as eq

def main(width):
  error = 0
  x, y, pairs, mylist = eq.allclear()
  while y < eq.width:
#    sleep(0.5) 
    next_list = eq.ylist(y, mylist)
    if y == eq.last and len(next_list) == 1:
      pairs.append(next_list[0])
      break 
    if len(next_list) > 0:
      x = next_list[eq.randselect(len(next_list))][0]
      mylist = eq.remove_list(x, y, mylist)
      pairs.append([x, y])
      y+=1
      print pairs
    else:
      error += 1
      print '{} times error!'.format(error) 
      x, y, pairs, mylist = eq.allclear()
  return pairs



x, y, pairs, mylist = eq.allclear()

pairs =  main(eq.width)
print pairs
