def algoritms(x,y,z):
  a=[x,y]
  for i in range(2,z):
    el=a[i-1]+a[i-1]
    a.append(el%10)
  b=a[-1]
  return b 