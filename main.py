import virkn
pirm,otr,skaits=input('Ievadi virknes pirmo skaitli, otro skaitli, kā arī virkns garumu, tos atdalot ar komatu: ').split(',')
print(virkn.n_el(int(pirm),int(otr),int(skaits)))