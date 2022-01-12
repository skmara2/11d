def total(x):
  summa=0
  for i in range(len(x)):
    b=x[i:]
    print(" "*i+b)
    summa+=int(b)
  print(summa)


        