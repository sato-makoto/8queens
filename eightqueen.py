#!/usr/bin/env python
import eightqueen_func as eq
import random

x, y, pairs, myset = eq.allclean()

pairs = eq.get_queens_pattern()
print pairs
