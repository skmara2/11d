def mazakais(l):
  ans = ''
  for f in sorted(l):
    if f!=0:
      ans+=str(f)
      l.remove(f)
      break
  for k in sorted(l):
    ans+=str(k)
  return ans