'''
Exercício 2
- Na área da eletrônica, em um circuito em série
temos que a resistência equivalente (total) desse
circuito é obtida mediante a soma de todas
as resistências existentes (RE = r1 + r2 + ... + rn).
- Faça uma aplicação que receba o valor de quatro
resistências ligadas em série, calcule e mostre a
resistência equivalente, a maior e a menor resistência.

--------------------------------------
Resistências fornecidas:
400, 300, 200, 700
A resistência equivalente é: 1600
A maior resistência é: 700
A menor resistência é: 200
--------------------------------------
'''

import locale
locale.setlocale(locale.LC_ALL,"")

print('Verificador de resistências')

r1 = int(input('Digite o valor da resistência 1: '))
r2 = int(input('Digite o valor da resistência 2: '))
r3 = int(input('Digite o valor da resistência 3: '))
r4 = int(input('Digite o valor da resistência 4: '))

maior = r1
menor = r1

if(r2>maior):
    maior = r2
if(r2<menor):
    menor = r2
if(r3>maior):
    maior = r3
if(r3<menor):
    menor = r3
if(r4>maior):
    maior = r4
if(r4<menor):
    menor = r4

print('Resistências fornecidas:')
print('{}, {}, {}, {}'.format(r1,r2,r3,r4))
print('A resistência equivalente é: {}'.format(r1+r2+r3+r4))
print('A maior resistência é: {}'.format(maior))
print('A menor resistência é: {}'.format(menor))