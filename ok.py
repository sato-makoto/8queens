#!/usr/bin/env python
from time import sleep
import delax_func as de
import eightqueen_func as eq

oklist = [ [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], 
           [1, 2],                         [1, 6],
           [2, 2], [2, 3], [2, 4], [2, 5], [2, 6],

           [4, 2], [4, 3], [4, 4], [4, 5], [4, 6],
                           [5, 4],
                   [6, 3],         [6, 5],   
           [7, 2],                         [7, 6]]

for x in range(5):
  de.ok_on(oklist, 1)
  sleep(0.3)
  de.ok_on(oklist, 0)
  sleep(0.3)
