'''
Exercício 3
- Faça uma aplicação que apresente em tela a tabuada
de qualquer número.
- O usuário fornece o número desejado e a classe
apresenta a relação de todos os cálculos de 1 a 10.
'''
import locale
locale.setlocale(locale.LC_ALL,"")

print('Gerador de tabuadas')

numero = int(input('Número que deseja gerar a tabuada: '))

for i in range(11):
    print('{} x {} = {}'.format(numero,i,i*numero))