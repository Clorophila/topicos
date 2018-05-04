import locale
import os
import csv
import json
locale.setlocale(locale.LC_ALL,"")

os.system('cls')

f = open("iris.csv","r")
iris = csv.reader(f)

lista = []

for linha in iris:    
    lista.append(linha)

f.close()

#print(lista)

irisjson = []

for linha in lista:
    if(linha==lista[0]):
        pass
    else:
        irisjson.append({chave:valor for (chave,valor) in zip(lista[0],linha)})

#print(json)

f = open('iris.json','w')
json.dump(irisjson,f,sort_keys=False,indent=4)
f.close()