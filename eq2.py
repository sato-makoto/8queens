#!/usr/bin/env python
from sys import argv
import eightqueen_func as eq

if len(argv) == 2 and argv[1].isdigit():
  eq.width = int(argv[1])

x, y, pairs, myset = eq.allclear()
mylist = eq.get_queens_pattern()

ynumstr = ''
for x in range(eq.width):
  ynumstr = ynumstr + ' ' + str(x)
ynumstr = '  ' + ynumstr

ylist = []
for x in range(eq.width):
  ylist.append('')

queen = u'\u2655'

xlist = []
pref = suff = ''
for x in range(eq.width):
  pref = '|' + ' |' * x
  suff = '| ' * (eq.width - 1 - x) + '|'
  xlist.append([pref,  suff])

for x in range(eq.width):
  yl = mylist[x][0]
  ylist[yl] = xlist[x][0] + queen + xlist[x][1]

# print ynumstr
num = 0
for x in ylist:
  print num, x
  num +=1
