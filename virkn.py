def n_el(a1,a2,n):
  if n==3:
    return int(str(a1+a2)[-1])
  elif n==2:
    return a2
  else:
    return int(str(n_el(a1,a2,n-1)+n_el(a1,a2,n-2))[-1])