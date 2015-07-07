import monte_8q_func as eqm

i = True
t = 0
while i:
  queens = eqm.queens()
  check = eqm.popcheck(queens)
  if check:
    print t, 'Times Fault and Success'
    print queens
    i = False
  else:
    i = True
    t+=1
#    print t, 'Times Fault'
