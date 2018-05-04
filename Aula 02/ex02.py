import locale
import os
locale.setlocale(locale.LC_ALL,"")

os.system('cls')

f = open("paises.txt","r")
paises = f.readlines()
f.close()
#print(paises)

for pais in paises:
   print(pais.strip('\n'))