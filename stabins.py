def numurs(x):
  summa=0
  for i in range (len(x)):
    y=x[i:]
    print(""+y)
    summa+=int(y)
  print(summa)