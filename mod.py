def stabins(a,i):
  if i==len(str(a))-1:
    return int(str(a)[-1])
  else:
    return int(str(a)[i:])+stabins(a,i+1)