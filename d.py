#!/usr/bin/env python
from time import sleep
import delax_func as de
import eightqueen_func as  eq

mylist = eq.makemylist()

de.on(mylist)
sleep(1)

eq.display_clear()
sleep(0.5)

de.on(mylist[::3])
sleep(2)
eq.display_clear()
