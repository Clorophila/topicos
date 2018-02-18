'''
Exercício 1
- Crie uma aplicação que receba o valor da base e da
altura de um triângulo retângulo e apresente na tela
sua área.
'''
import locale
locale.setlocale(locale.LC_ALL,"")

print('Calculadora de áreas')

base = float(input('Digite o valor da base do triângulo: ').replace(',','.'))
altura = float(input('Digite o valor da altura do triângulo: ').replace(',','.'))

print('A área do triângulo é de {}'.format(round(base*altura,2)))