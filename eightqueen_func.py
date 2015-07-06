import random

def q0(x, y):
  if (x == 0) or (y == 7):
    return False
  else:
    return True

def q1(x, y):
  if (x == 7) or (y == 7):
    return False
  else:
    return True

def makemyset(myset):
  for f1 in range(8):
    for f2 in range(8):
      pair = '{}-{}'.format(f1, f2)
      myset.add(pair)
  return myset

def delpair(x, y, setz):
  pair = '{}-{}'.format(x, y)
  if pair in setz:
    setz.remove(pair)
  
def delx(x, setz):
  for y in range(8):
    delpair(x, y, setz)

def dely(y, setz):
  for x in range(8):
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
      templist.insert(1,z)
  return templist

def rest_line_length(y, setz):
  templist = []
  for z in setz:
    if z[2] == str(y):
      templist.insert(1,z)
  return len(templist)

def allclean():
  x  = randselect(8)
  y = 0
  pairs = []
  myset = set()
  makemyset(myset)
  return x, y, pairs, myset

def get_queens_pattern():
  x, y, pairs, myset = allclean()
  while y < 8:
    if y == 7 and rest_line_length(y, myset) == 1:
      temp = myset.pop()
      x, y = int(temp[0]), int(temp[2])
      pairs.insert(10, [x, y])
      break
    else:
      if rest_line_length(y, myset):
        mybatch(x, y, myset)
        pairs.insert(10,[x, y])
        y+=1
        yline = ylines(y, myset)
        ylength = len(yline)
        if ylength:
          x = int(yline[randselect(ylength)][0])
      else:
        x, y, pairs, myset = allclean()
  return  pairs
