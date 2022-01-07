def elem(a,b,c):
  l=[a,b]
  for i in range(2,c):
    el=l[i-1]+l(i-2)
    l.append(el%10)
  print(l)