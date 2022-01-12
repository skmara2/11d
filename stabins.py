import math
def total(x):
  z=0
  for i in range(len(x)):
    y=x[i:]
    print(" "*i +y)

    z+=int(y)
  print(z)
