def cipars(a,b,n):
  d=[a,b]
  for i in range(n-2):
    t=int(d[-1])+int(d[-2])
    d.append(t%10)
  return t%10