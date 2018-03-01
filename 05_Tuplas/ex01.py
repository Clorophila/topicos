'''
Exercício 1
- Faça um programa que carregue um vetor de seis
elementos numéricos inteiros, calcule e mostre:
    • A quantidade de números pares
    • Quais números são ímpares
    • A soma dos números
    • O maior número
    • O menor número
    • A quantidade de números positivos
'''
lista = []

for n in range(6):
    while True:
        try:
            valor = int(input('Digite o valor do número {}: '.format(n+1)))
            break
        except:
            print('Valor digitado inválido. Digite um número inteiro.')
    lista.append(valor)
tupla = tuple(lista)
pares = 0
impares = 0
soma = sum(tupla)
menor = min(tupla)
maior = max(tupla)
for valor in tupla:
    if valor%2==0:
        pares+=1
    else:
        impares+=1
print('Tupla dos valores: {}'.format(tupla))
print('Quantidade de pares = {}'.format(pares))
print('Quantidade de impares = {}'.format(impares))
print('Soma dos números digitados = {}'.format(soma))
print('Menor número digitado = {}'.format(menor))
print('Maior número digitado = {}'.format(maior))