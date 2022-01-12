def n_elements(a1, a2, n):
  for i in range(n-2):
    a3 = (a1+ a2) % 10
    a1 = a2
    a2 = a3
  return a2


def saskaitisana_stabina(n):
  kopa = 0
  for i in range(len(n)):
    kopa += int(n[i:])
    print(" " * i + n[i:])
  print("-" * len(n))
  print(kopa)