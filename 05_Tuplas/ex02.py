'''
Exercício 2
- Uma imagem é formada por pixels. Considere uma
imagem com dimensão de 10 x 10 e faça uma
aplicação que contenha um estrutura bidimensional
com essas dimensões.
- A seguir, para cada posição da estrutura bidimensional
armazene um valor aleatório entre 0 e 255 (esses
valores correspondem às tonalidades aplicadas sobre
a imagem).
- Apresente em tela os valores gerados.
'''
import random

matrix = tuple([])
for i in range(10):
    linha = []
    for j in range(10):
        linha.append(random.randrange(0,256,1))
    matrix = matrix + (linha,)

for linha in matrix:
    print(linha)