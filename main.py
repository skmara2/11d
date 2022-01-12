import mod
"""
# 2.uzdevums
a1 = int(input("Ievadi 1.elementu: "))
a2 = int(input("Ievadi 1.elementu: "))
n = int(input("Ievadi kuru elementu atrast: "))
print(mod.n_elements(a1, a2, n))
"""
# 3.uzdevums
n = input("Ievadi skaitli, bez nullēm: ")
kopa = 0
for i in range(len(n)):
  kopa += int(n[i:])
  print(" " * i + n[i:])
print("-" * len(n))
print(kopa)