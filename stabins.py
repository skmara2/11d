def summa(x):
  s=0
  for i in range(len(x)):
    y=x[i:]
    print(" "*i+y)
    s+=int(y)
  print("_"*len(x))
  print(s)