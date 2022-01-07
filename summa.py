def summa():
  total=0
  x=input("ievadi skaitli: ")
  for i in range(len(x)):
    total+=int(x[i:])
  return total
