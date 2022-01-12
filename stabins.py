def tot(x):
  summa=0
  for i in range(len(x)):
    y=x[i:]
    print(" "*i+y)
    summa+=int(y)
  print("-------") 
  print(summa)
  return summa
