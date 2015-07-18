#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from time import sleep
import eightqueen_func as eq

def main(width):
  error = 0
  x, y, pairs, mylist = eq.allclear()
  while y < eq.width:
#    sleep(0.5) 
    next_list = eq.ylist(y, mylist)
    if len(next_list) > 0:
      x = next_list[eq.randselect(len(next_list))][0]
      mylist = eq.remove_list(x, y, mylist)
      pairs.append([x, y])
      temp = pairs[:]
      y+=1
#      for z in range(eq.width - y):
#         temp.append([None, None])
      print temp
    else:
      error += 1
      print '{} times error!'.format(error) 
      print ''
      x, y, pairs, mylist = eq.allclear()
  return pairs, error

x, y, pairs, mylist = eq.allclear()

pairs, error =  main(eq.width)
print '{}回のエラーを経て、ようやくできました'.format(error)
print pairs
