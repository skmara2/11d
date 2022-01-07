def n_elements(a1, a2, n):
  for i in range(n-2):
    a3 = (a1+ a2) % 10
    a1 = a2
    a2 = a3
  return a2