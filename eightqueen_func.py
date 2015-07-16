import random

from sys import argv
if len(argv) == 2 and argv[1].isdigit() and int(argv[1]) > 3:
  width = int(argv[1])
else:
  width = 8

last = width - 1

def randselect(n):
  random.seed()
  return random.randrange(0,n)

def allclear():
  x, y = 0, 0
  pairs = []
  mylist = []
  mylist = makemylist()
  return x, y, pairs, mylist

def makemylist():
  listz = []
  for f1 in range(width):
    for f2 in range(width):
      listz.append([f1, f2])
  return listz

def ylist(y, all_list):
  tlist = []
  for l in all_list:
     if l[1] == y:
        tlist.append(l)
  return tlist
       
def remove_list(x, y, all_list):
  temp = all_list[:]
  for l in all_list:
    if temp.count(l) and l[0] == x:
      temp.remove(l)
    if temp.count(l) and l[1] == y:
      temp.remove(l)
    if temp.count(l) and (abs(l[0] - x) == abs(l[1] - y)):
      temp.remove(l)
  return temp


def main(width):
  x, y, pairs, mylist = allclear()
  while y < width:
    next_list = ylist(y, mylist)
    if len(next_list) > 0:
      x = next_list[randselect(len(next_list))][0]
      mylist = remove_list(x, y, mylist)
      pairs.append([x, y])
      y+=1
    else:
      x, y, pairs, mylist = allclear()
  return pairs
