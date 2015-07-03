#!/usr/bin/env python
import eightqueen_func as eq
import random

x, y, pairs, myset = eq.allclean()

while y < 8:
  if y == 7 and eq.rest_line_length(y, myset) == 1:
    pairs.add(myset.pop())
    break
  else:
    if eq.rest_line_length(y, myset):
      eq.mybatch(x, y, myset)
      pairs.add('{}-{}'.format(x, y)) 
      y+=1
      ylines = eq.ylines(y, myset)
      ylength = len(ylines)
      if ylength:
        x = int(ylines[eq.randselect(ylength)][0])
    else:
      x, y, pairs, myset = eq.allclean()

for x in pairs:
  print x
