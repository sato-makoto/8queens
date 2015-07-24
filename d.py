#!/usr/bin/env python
from time import sleep
import delax_func as de
import eightqueen_func as  eq

mylist = eq.makemylist()

de.line_on_off(3, 0.1, 1)
de.line_on_off(3, 0.1, 0)

"""
de.on(mylist)
sleep(1)

eq.display_clear()
sleep(0.5)

alist = [[5, 5], [2, 7], [4,3]]
for x in range(10):
  de.on(alist)
  sleep(0.4)
  eq.display_clear()
  de.neg_on(alist)
  sleep(0.2)
  eq.display_clear()
"""

