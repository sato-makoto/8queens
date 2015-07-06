#!/usr/bin/env python
import eightqueen_func as eq

x, y, pairs, myset = eq.allclean()
mylist = eq.get_queens_pattern()

ynumstr ="   0 1 2 3 4 5 6 7"
ylist = ['', '', '', '', '', '', '', '']
queen = 'Q'

xlist = []
pref = suff = ''
for x in range(8):
  pref = '|' + ' |' * x
  suff = '| ' * (7 - x) + '|'
  xlist.append([pref,  suff])

for x in range(8):
  yl = mylist[x][0]
  ylist[yl] = xlist[x][0] + queen + xlist[x][1]

print ynumstr
num = 0
for x in ylist:
  print num, x
  num +=1
