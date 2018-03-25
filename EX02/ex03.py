'''
Exercício 3: Escreva um programa que recebe sequencia
de palavras separados por vírgula e apresenta na tela
as palavras ordenadas.
'''
string_list = input().split(',')

for word in string_list:
    print(word,end=' ')

string_list.sort()

print('Lista ordenada: ')
for word in string_list:
    print(word,end=' ')