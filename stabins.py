def total(x):
  summa=0
  for i in range(len(x)):
    y=x[i:]
    summa+=int(y)
    print(" "*i+y)
  print("-"*len(x))
  print(summa)