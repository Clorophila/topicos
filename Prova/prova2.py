import random
import string
import os
import operator

class Pet:
    pets = {}
    def __init__(self,id,nome,especie,raca,nascimento,sexo):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.nascimento = nascimento
        self.sexo = sexo

def criar_pet(pets):
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
        print('Nome: {}'.format(pet[nome]))
        print('Espécie: {}'.format(pet[especie]))
        print('Raça: {}'.format(pet[raca]))
        print('Nascimento: {}'.format(pet[nascimento]))
        print('Sexo: {}'.format(pet[sexo]))
        print('----------------------------------')
        print('\n{} do pet: '.format(key),end='')
        pet[key] = input()
    print(pet)






    nome = input('-> Digite seu nome: ')
    id = len(users)+1
    try:
        users.append(Usuario(nome,id))
        print('ID: {}'.format(users[-1].id))
        print('Nome: {}'.format(users[-1].name))
        print('Usuário: {}'.format(users[-1].username))
        print('senha: {}'.format(users[-1].password))
        input()
    except:
        print('Erro ao criar o usuário.')

def listar_usuarios(users,chave):
    os.system('clear')
    print('{0:5} | {1:15} | {2:15} | {3}'.format('ID','Username','Senha','Nome'))
    users_ordenado = sorted(users, key=operator.attrgetter(chave))
    for usuario in users_ordenado:
        print('{0:5} | {1:15} | {2:15} | {3}'.format(usuario.id,usuario.username,usuario.password,usuario.name))
    input()

sair = False
users = []

while not sair:
    menu()
    op = input('-> Digite a opção desejada: ')
    if op == '1':
        criar_usuario(users)
    elif op == '2':        
        while True:
            try:
                print('Ordenar por Id: 1, Nome: 2, Username: 3 ')
                op = input()
                if op == '1':
                    listar_usuarios(users,'id')
                    break
                if op == '2':
                    listar_usuarios(users,'name')
                    break
                if op == '3':
                    listar_usuarios(users,'username')
                    break
                else:
                    raise ValueError()
            except ValueError:
                print('Valor inválido!')        
    elif op == '0':
        sair = True



class Pet():
    def __init__(nome,especie,raca,nascimento,sexo):
        self.id = ''
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.nascimento = nascimento
        self.sexo = sexo