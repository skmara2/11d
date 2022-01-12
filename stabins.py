#stabins.py
def total(x):
  z=0
  for i in range(len(x)):
    y=x[i:]
    print(" "*i+y)
    z+=int(y)
  print(z)


#2.uzd    algoritms.py
#def algoritms(x,y,z):
  #a=[x,y]
  #for i in range(2,z):
    #el=a[i-1]+a[i-1]
    #a.append(el%10)
  #b=a[-1]
  #return b 