#!/usr/bin/env python
import random
import time
import eightqueen_func as eq

def get_deb_queens_pattern():
  print "{} Queens Start!".format(eq.width)
  i = 0
  x, y, pairs, myset = eq.allclear()
  while y < eq.width:
    time.sleep(0.5)
    if y == eq.width - 1 and eq.rest_line_length(y, myset) == 1:
      temp = myset.pop()
      x, y = int(temp[0]), int(temp[2])
      pairs.append([x, y])
      print "After {} times Fault, Now Success!".format(i)
      break
    else:
      if eq.rest_line_length(y, myset):
        eq.mybatch(x, y, myset)
        pairs.append([x, y])
        print pairs
        y+=1
        yline = eq.ylines(y, myset)
        ylength = len(yline)
        if ylength:
          x = int(yline[eq.randselect(ylength)][0])
      else:
        i+=1
        print i, "Times Fault!" 
        x, y, pairs, myset = eq.allclear()
  return  pairs


x, y, pairs, myset = eq.allclear()

pairs =  get_deb_queens_pattern()
print pairs

