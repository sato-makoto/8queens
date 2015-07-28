#!/usr/bin/env python
from time import sleep
import delax_func as de
import eightqueen_func as eq

nolist = [ [0, 2], [0, 3], [0, 4], [0, 5], 
           [1, 3],                         
            [2, 4],
           [3, 2], [3, 3], [3, 4], [3, 5],

            [5, 3], [5, 4], [5, 5],
                   [6, 3],         [6, 5],   
            [7, 3], [7, 4], [7, 5]]

for x in range(5):
  de.ok_on(nolist, 1)
  sleep(0.3)
  de.ok_on(nolist, 0)
  sleep(0.3)
