import random
from sys import argv

if len(argv) == 2 and argv[1].isdigit() and int(argv[1]) > 3:
  width = int(argv[1])
else:
  width = 8

def queens():
  yset = [x for x in range(width)]
  queens = []
  for x in range(width):
    y = randselect(width-x)
    queens.append([x, yset.pop(y)])
  return queens
  
def randselect(n):
  random.seed()
  return random.randrange(n)

def queencheck(list0, list1):
  if abs(list0[0] - list1[0]) == abs(list0[1] - list1[1]):
    return False
  else:
    return True

def popcheck(qlist):
  listcopy = qlist[:]
  while len(listcopy):
    x = listcopy.pop()
    for y in listcopy:
       tf = queencheck(x, y)
       if not tf:
          return False
          break
  return True
