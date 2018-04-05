'''
Exercício 1: Escreva um programa que recebe, pelo console,
uma sequencia de números separados por vírgula e gera uma
lista e uma tupla contendo todos estes números.
'''
lista = [*map(int,input().split(','))]
tupla = tuple(lista)

print(lista)
print(tupla)