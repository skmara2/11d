def mazakais():
  n=input("ievadi: ")
  jaunais=""
  list=[]
  for i in range(len(n)):
    list.append(int(n[i]))
  list.sort()
  for i in range(len(list)):
    if list[i]==0:
      continue
    else:
      jaunais+=str(list[i])
      list.pop(i)
      break
  for i in range(len(list)):
    jaunais+=str(list[i])
    






  return jaunais