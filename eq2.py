#!/usr/bin/env python
# -*- coding: utf-8 -*-

import eightqueen_func as eq

x, y, pairs, mylist = eq.allclear()

mylist = eq.main(eq.width)

ynumstr = ''
for x in range(eq.width):
  ynumstr = ynumstr + ' ' + str(x)
ynumstr = '  ' + ynumstr

ylist = []
for x in range(eq.width):
  ylist.append('')

def queen_w_b(y):
  if y%2:
    return '♕'
  else:
    return '♛'

xlist = []
pref = suff = ''
for x in range(eq.width):
  pref = '|' + ' |' * x
  suff = '| ' * (eq.width - 1 - x) + '|'
  xlist.append([pref,  suff])

for y in range(eq.width):
  yl = mylist[y][0]
  queen = queen_w_b(y)
  ylist[yl] = xlist[y][0] + queen + xlist[y][1]

print ynumstr
num = 0
for x in ylist:
  print num, x
  num +=1
