'''
Exercício 2
- Crie um programa para calcular e exibir na tela o peso
ideal. IMC = (peso / (altura^2))
'''
import locale
locale.setlocale(locale.LC_ALL,"")

print('Calculadora de peso ideal')
altura = float(input('Digite o valor da sua altura (em metros): ').replace(',','.'))

'''
Tabela de peso ideal pelo IMC (OMS)
--------------------------------------------
Situação                    IMC em adultos
abaixo do peso ideal        abaixo de 18,5
no peso ideal               entre 18,5 e 25
acima do peso ideal         entre 25 e 30
obeso                       acima de 30
--------------------------------------------
Desse modo, o peso ideal é a faixa cujo IMC fica entre 18,5 e 25.
Como IMC = Peso / Altura², o peso ideal pode ser calculado pela relação:

Peso = IMC x Altura²
'''
peso_minimo = round(18.5 * altura**2,2)
peso_maximo = round(25 * altura**2,2)
print('O seu peso ideal (IMC entre 18,5 e 25) é {0:.2f} e {1:.2f} quilos.'.format(peso_minimo,peso_maximo))