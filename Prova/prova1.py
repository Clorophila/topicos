'''
Aluno: Welton Antonio Gomes
RA: 2840481713038

Prova - Tópicos Especiais em Informática
26/04/2018

'''
# Definições gerais
import locale
import os
import json
from operator import itemgetter, attrgetter
locale.setlocale(locale.LC_ALL,"")


'''
Questão 1 - Menu:
'''
def menu():
    os.system('cls')
    print('')
    while(True):
        print('------------ Pet Shop ------------')
        print('[1] Adicionar Pet')
        print('[2] Relatório de Pet')
        print('[3] Relatório de Pet por Espécie')
        print('[4] Exportar dados')
        print('[0] Sair')
        print('----------------------------------')
        print('\nDigite a opção desejada: ',end='')

        try:
            opt = int(input())
            if(opt<0 or opt>4):
                raise ValueError
            else:
                break
        except ValueError:
            os.system('cls')
            print('Valor inválido. Por favor digite um valor válido.')

    return opt

'''
Questão 2 - Função Adicionar Pet:

'''

def adicionar_pet(pets):
    id = len(pets)+1
    pet = {        
        'nome' : '',
        'especie' : '',
        'raca' : '',
        'nascimento' : '',
        'sexo' : '',
    }
        
    for key in pet:
        os.system('cls')
        print('------------ Criar Pet ------------')
        print('ID: {}'.format(id))
        print('Nome: {}'.format(pet['nome']))
        print('Espécie: {}'.format(pet['especie']))
        print('Raça: {}'.format(pet['raca']))
        print('Nascimento: {}'.format(pet['nascimento']))
        print('Sexo: {}'.format(pet['sexo']))
        print('----------------------------------')
        print('\n{} do pet: '.format(key),end='')
        pet[key] = input()
    pet['id'] = id
    return pet

'''
Questão 3 - Relatório de Pets:

'''

def relatorio_pet(pets,chave,especie):
    os.system('cls')
    print('{0:5} | {1:10} | {2:10} | {3:10} | {4:10} | {5}'.format('ID','Nome','Espécie','Raça','Nascimento','Sexo'))
    pets_ordenado = sorted(pets, key=itemgetter(chave))
    if(especie=='todas'):
        for pet in pets_ordenado:        
            print('{0:5} | {1:10} | {2:10} | {3:10} | {4:10} | {5}'.format(pet['id'],pet['nome'],pet['especie'],pet['raca'],pet['nascimento'],pet['sexo']))
    elif(especie=='cao'):
        for pet in pets_ordenado:
            if(pet['especie']=='cao'):
                print('{0:5} | {1:10} | {2:10} | {3:10} | {4:10} | {5}'.format(pet['id'],pet['nome'],pet['especie'],pet['raca'],pet['nascimento'],pet['sexo']))
    elif(especie=='gato'):
        for pet in pets_ordenado:
            if(pet['especie']=='gato'):
                print('{0:5} | {1:10} | {2:10} | {3:10} | {4:10} | {5}'.format(pet['id'],pet['nome'],pet['especie'],pet['raca'],pet['nascimento'],pet['sexo']))
    else:
        for pet in pets_ordenado:
            if(pet['especie']!='gato' and pet['especie']!='cao'):
                print('{0:5} | {1:10} | {2:10} | {3:10} | {4:10} | {5}'.format(pet['id'],pet['nome'],pet['especie'],pet['raca'],pet['nascimento'],pet['sexo']))
    input()

'''
Questão 4 - Relatório por espécie:
'''
def relatorio_pet_especie(pets):
    os.system('cls')
    print('')
    while(True):
        print('------------ Pet Shop ------------')
        print('[1] Cachorros')
        print('[2] Gatos')
        print('[3] Todos')
        print('[4] Outros')
        print('[0] Sair')
        print('----------------------------------')
        print('\nDigite a opção desejada: ',end='')

        try:
            opt = int(input())
            if(opt<0 or opt>4):
                raise ValueError
            else:
                break
        except ValueError:
            os.system('cls')
            print('Valor inválido. Por favor digite um valor válido.')

    if(opt==1):
        relatorio_pet(pets,'nome','cao')
    elif(opt==2):
        relatorio_pet(pets,'nome','gato')
    elif(opt==3):
        relatorio_pet(pets,'nome','todas')
    elif(opt==4):
        relatorio_pet(pets,'nome','outras')

'''
Questão 5 - Exportar dados para um JSON:
'''
def exportar(pets):
    dir_original = os.getcwd()

    dir = os.path.join(os.sep,os.environ["HOMEPATH"],'Desktop','dados')
    if(not os.path.exists(dir)):
        os.makedirs(dir)    
    os.chdir(dir)

    f = open('arquivo.json','w')
    json.dump(pets,f,sort_keys=False,indent=4)
    f.close()

    os.chdir(dir_original)

#-----------------------------------------------------------------
#Execução do programa:

#Lista para armazenar os vários pets, inicialmente vazia
pets = []

sair = False

while not sair:
    opt = menu()

    if(opt==1):
        pets.append(adicionar_pet(pets))
    elif(opt==2):
        relatorio_pet(pets,'nome','todas')
    elif(opt==3):
        relatorio_pet_especie(pets)
    elif(opt==4):
        exportar(pets)
    else:
        sair = True
