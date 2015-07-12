#!/usr/bin/env python
import step_func as step

print step.randselect()

print step.new_queen(3)

mylist = []
for x in range(4):
  for y in range(4):
    mylist.append([x, y])

print mylist

for x in mylist:
  templist = mylist[:]
  templist.pop(x[0])
  for y in templist:
    print x, y, step.compare(x,y)
