#!/usr/bin/env python
# -*- coding: utf-8 -*-

import eightqueen_func as eq

x, y, pairs, myset = eq.allclear()
mylist = eq.get_queens_pattern()

ynumstr = ''
for x in range(eq.width):
  ynumstr = ynumstr + ' ' + str(x)
ynumstr = '  ' + ynumstr

ylist = []
for x in range(eq.width):
  ylist.append('')

queen = '♕'

xlist = []
pref = suff = ''
for x in range(eq.width):
  pref = '|' + ' |' * x
  suff = '| ' * (eq.width - 1 - x) + '|'
  xlist.append([pref,  suff])

for x in range(eq.width):
  yl = mylist[x][0]
  ylist[yl] = xlist[x][0] + queen + xlist[x][1]

print ynumstr
num = 0
for x in ylist:
  print num, x
  num +=1
