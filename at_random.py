import at_random_func as atm

i = True
t = 0
while i:
  queens = atm.queens()
  check = atm.popcheck(queens)
  if check:
    print t, 'Times Fault and Success'
    print queens
    i = False
  else:
    i = True
    t+=1
    print t, 'Times Fault'
