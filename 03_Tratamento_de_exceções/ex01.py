'''
Exercício 1
- Elabore uma aplicação o peso e altura de um número
indeterminado de pessoas.
- Utilize tratamento de exceção para garantir que os
valores informados são válidos.
- Após a entrada correta dos dados apresente o IMC.
'''
import locale
locale.setlocale(locale.LC_ALL,"")

print('Calculadora de IMC')

continuar = True

while(continuar):
    while(True):
        try:
            peso = float(input('Digite o valor do seu peso (em Kg): ').replace(',','.'))
            if(peso<0):
                raise ValueError
            break
        except ValueError:
            print('Valor inválido. Por favor digite um número positivo.')

    while(True):
        try:
            altura = float(input('Digite o valor da sua altura (em metros): ').replace(',','.'))
            if(altura<0):
                raise ValueError
            break
        except ValueError:
            print('Valor inválido. Por favor digite um número positivo.')

    print('O seu IMC é {:.2f}.'.format(peso/(altura**2)))

    while(True):
        try:
            opcao = input('Deseja calcular para mais uma pessoa? (s/n): ').lower()
            if(opcao=='n'):
                continuar=False
            elif(opcao=='s'):
                pass
            else:
                raise ValueError
            break
        except ValueError:
            print('Valor inválido.')