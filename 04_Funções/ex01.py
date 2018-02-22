'''
Exercício 1
- Elabore uma aplicação receba um número
indeterminado de valores informados pelo usuário.
- Crie funções para determinar:
    • Quantidade de números pares
    • Quais são os números ímpares
    • O maior número
    • O menor número
    • A média dos números
- Apresente os resultados na tela.
'''
def pares(numeros):
    n_pares = 0
    for n in numeros:
        if n%2==0:
            n_pares += 1
    return n_pares

def impares(numeros):
    n_impares = 0
    for n in numeros:
        if n%2==1:
            n_impares += 1
    return n_impares

def maior(numeros):
    maior_n = numeros[0]
    for n in numeros:
        if n>maior_n:
            maior_n = n
    return maior_n

def menor(numeros):
    menor_n = numeros[0]
    for n in numeros:
        if n<menor_n:
            menor_n = n
    return menor_n

def media(numeros):
    return sum(numeros) / len(numeros)

continuar = True
numeros = []

while(continuar):
    while(True):
        try:
            entrada = input('Digite um número: ')
            if not entrada.isdigit():
                raise ValueError
            else:
                numeros.append(int(entrada))
            break
        except ValueError:
            print('Valor inválido. Por favor digite um número inteiro.')

    while(True):
        try:
            opcao = input('Deseja adicionar mais números? (s/n): ').lower()
            if(opcao=='n'):
                continuar=False
            elif(opcao=='s'):
                pass
            else:
                raise ValueError
            break
        except ValueError:
            print('Valor inválido.')

print('Valores digitados:')
for n in numeros:
    if n is numeros[-1]:
        print('{}'.format(n))
    elif n is numeros[-2]:
        print('{}'.format(n), end=' e ')
    else:
        print('{}'.format(n), end=', ')

print('Quantidade de números pares: {}'.format(pares(numeros)))
print('Quantidade de números ímpares: {}'.format(impares(numeros)))
print('Maior número digitado: {}'.format(maior(numeros)))
print('Menor número digitado: {}'.format(menor(numeros)))
print('Média dos números digitados: {:.2f}'.format(media(numeros)))