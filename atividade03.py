'''
Exercício 3
- Uma farmácia precisa ajustar os preços de seus
produtos em 12%. Elabore uma aplicação que receba
o valor do produto e aplique o percentual de
acréscimo.
- O novo valor a ser calculado deve ser arredondado e
apresentado com duas casas decimais.
'''
import locale
locale.setlocale(locale.LC_ALL,"")

print('Conversor de preços')
valor = float(input('Digite o valor atual do produto: ').replace(',','.'))
print('O valor do produto ajustado de 12% é de: {}'.format(locale.currency(valor*1.12)))