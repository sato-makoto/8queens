import random
from sys import argv

if len(argv) == 2 and argv[1].isdigit() and int(argv[1]) > 3:
  width = int(argv[1])
else:
  width = 8

def randselect():
  random.seed()
  return random.randrange(width)

def new_queen(x):
  return [x, randselect(),] 
