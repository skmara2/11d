def virkne(x,y,z):
  list=[x,y]
  for i in range(2,z):
    list.append((list[i-1]+list[i-2])%10)
  return list[-1]