'''
Exercício 2: Escreva um programa que recebe dois números
inteiros (i,j) e gera um array 2D. O valor de i é referente
as linhas e j as colunas.
'''
from random import randint

i,j = map(int,input().split(','))

matrix = [[0]*j]*i

print(matrix)