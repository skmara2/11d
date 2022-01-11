def cip(n):
  t=[(str(n)).split]
  print(t)
  g=[]
  for i in range (0,len(t)):
    print(i)
    if i==1 and t[i]==0:
      continue
    if int(t[i-1])<int(t[i]):
      g.append(t[i-1])
    else:
      g.append(t[i])
      print(t[i])
    return g

