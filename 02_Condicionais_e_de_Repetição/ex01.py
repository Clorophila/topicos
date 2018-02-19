'''
Exercício 1
- Elabore uma aplicação que receba o nome de um
produto e o seu valor. O desconto deve ser calculado
de acordo com o valor fornecido conforme a Tabela.
- Apresente em tela o nome do produto, valor original
do produto e o novo valor depois de ser realizado o
desconto. Caso o valor digitado seja menor que zero,
deve ser emitida uma mensagem de aviso.
----------------------------------
Valor               Desconto (%)
>= 50 e < 200       5
>= 200 e <500       6
>= 500 e <1000      7
>= 1000             8
----------------------------------
'''
import locale
locale.setlocale(locale.LC_ALL,"")

print('Calculadora de descontos')

nome = input('Digite o nome do produto: ')
valor_original = float(input('Digite o valor do produto: ').replace(',','.'))

while(valor_original<0):
    valor_original = float(input('Valor inválido. Digite novo valor: ').replace(',','.'))

if(valor_original<50):
    desconto = 0
elif(valor_original>=50 and valor_original<200):
    desconto = 0.05
elif(valor_original>=200 and valor_original<500):
    desconto = 0.06
elif(valor_original>=500 and valor_original<1000):
    desconto = 0.07
else:
    desconto = 0.08

valor_desconto = valor_original * (1-desconto)

print('Produto: {}'.format(nome))
print('Valor original: {}'.format(locale.currency(valor_original)))
print('Valor com desconto: {}'.format(locale.currency(valor_desconto)))