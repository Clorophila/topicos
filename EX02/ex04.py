'''
Exercício 4: Escreva um programa que recebe
sequencia e calcula a quantidade de letras e dígitos.
'''
lista = input().split()

letras = 0
digitos = 0

for item in lista:
    if item.isnumeric():
        digitos += 1
    elif item.isalpha():
        letras += 1

print('Quantidade de letras: {}'.format(letras))
print('Quantidade de dígitos: {}'.format(digitos))