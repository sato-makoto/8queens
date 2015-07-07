import random

width = 8

def queens():
  queens = []
  for i in range(width):
    x = randselect(width)
    y = randselect(width)
    queens.append([x, y])
  return queens
  
def randselect(n):
  random.seed()
  return random.randrange(n)

def xycheck(list0, list1):
  if list0[0] == list1[0] or list0[1] == list1[1]:
    return False
  else:
    return True


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
       tf = queencheck(x, y) and xycheck(x, y)
       if not tf:
          return False
          break
  return True
