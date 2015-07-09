import random

from sys import argv
if len(argv) == 2 and argv[1].isdigit() and int(argv[1]) > 3:
  width = int(argv[1])
else:
  width = 8

last = width - 1

def q0(x, y):
  if (x == 0) or (y == last):
    return False
  else:
    return True

def q1(x, y):
  if (x == last) or (y == last):
    return False
  else:
    return True

def makemyset():
  setz = set()
  for f1 in range(width):
    for f2 in range(width):
      pair = '{}-{}'.format(f1, f2)
      setz.add(pair)
  return setz

def delpair(x, y, setz):
  pair = '{}-{}'.format(x, y)
  if pair in setz:
    setz.remove(pair)
  
def delx(x, setz):
  for y in range(width):
    delpair(x, y, setz)

def dely(y, setz):
  for x in range(width):
    delpair(x, y, setz)

def delplus(x, y, setz):
  while(q0(x, y)):
   x-=1
   y+=1
   delpair(x, y, setz)

def addplus(x, y, setz):
  while(q1(x, y)):
   x+=1
   y+=1
   delpair(x, y, setz)

def mybatch(x, y, zset):
  delpair(x, y, zset)
  delx(x, zset)
  dely(y, zset)
  delplus(x, y, zset)
  addplus(x, y, zset)

def randselect(n):
  random.seed()
  return random.randrange(0,n)

def selectfault(setz):
  if len(setz):
    return True
  else:
    return False

def ylines(y, setz):
  templist = []
  for z in setz:
    if z[2] == str(y):
      templist.append(z)
  return templist

def rest_line_length(y, setz):
  templist = []
  for z in setz:
    if z[2] == str(y):
      templist.append(z)
  return len(templist)

def allclear():
  x  = randselect(width)
  y = 0
  pairs = []
  myset = set()
  myset = makemyset()
  return x, y, pairs, myset

def get_queens_pattern():
  x, y, pairs, myset = allclear()
  while y < width:
    if y == last and rest_line_length(y, myset) == 1:
      temp = myset.pop()
      x, y = int(temp[0]), int(temp[2])
      pairs.append([x, y])
      break
    else:
      if rest_line_length(y, myset):
        mybatch(x, y, myset)
        pairs.append([x, y])
        y+=1
        yline = ylines(y, myset)
        ylength = len(yline)
        if ylength:
          x = int(yline[randselect(ylength)][0])
      else:
        x, y, pairs, myset = allclear()
  return  pairs
