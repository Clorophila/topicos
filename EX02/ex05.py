'''
Exercício 5: Escreva um programa que recebe sequencia
e calcula a quantidade de letras maiúsculas e minúsculas
'''
lista = input().split()

maiusculas = 0
minusculas = 0

for item in lista:
    if item.isupper():
        maiusculas += 1
    elif item.islower():
        minusculas += 1

print('Quantidade de maiúsculas: {}'.format(maiusculas))
print('Quantidade de minúsculas: {}'.format(minusculas))