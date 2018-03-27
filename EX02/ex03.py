'''
Exercício 3: Escreva um programa que recebe sequencia
de palavras separados por vírgula e apresenta na tela
as palavras ordenadas.
'''
string_list = input().replace(' ','').split(',')

for word in string_list:
    print(word,end=' ')

string_list.sort()

print('Lista ordenada: ')

for word in string_list:
    if word!= string_list[-1]:
        print(word,end=', ')
    else
        print(word)