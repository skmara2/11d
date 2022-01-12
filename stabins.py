
def virkne(x,y,z):
  list=[x,y]
  for i in range(2,z):
    list.append((list[i-1]+list[i-2])%10)
  return list[-1]

def total(x):
  z=0
  for i in range(len(x)):
    y=x[i:]
    print(" "*i+y)
    z+=int(y)
  print("-"*len(x))
  print(z)