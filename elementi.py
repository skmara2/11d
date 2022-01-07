def virkne(a,b,z):
  b = [a,b]
  for i in range(2,z):
    b.append((b[i-1]+b[i-2])%10)
  return b[-1]