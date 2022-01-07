def elem(z,x,y):
  l=[z,x]
  for i in range(2,y):
    el=l[i-1]+l[i-2]
    l.append(el%10)
  print(l[-1])