'''
Exercício 1
- Faça um programa capaz de gerar usernames e
senhas para alunos da FATEC de Ribeirão Preto.
- O programa recebe como entrada o nome completo
do aluno e produz um username contendo:
    • A primeira letra do nome e o sobrenome
- O resultado deve ser armazenado em um estrutura da
sua preferência: Tupla, Lista, Dicionário ou Conjunto.
- O programa deve garantir que não sejam gerados.
username duplicados
- As senhas provisórias deve conter no mínimo 8
caracteres (números, letras e símbolos) com máxima
segurança.
'''
import random
import string
import os
import operator

class Usuario:
    usuarios = {}
    def __init__(self,name,id):
        self.id = id
        self.name = name
        self.username = self.gerar_username()
        self.password = Usuario.gerar_password()
        Usuario.usuarios.update({self.username:self.password})
        self.flagsenha = True

    def gerar_username(self):
        nomes = self.name.lower().split()        
        username = nomes[0][0]
        if nomes[-1] == 'jr' or nomes[-1] == 'junior' or nomes[-1] == 'júnior' or nomes[-1] == 'filho' or nomes[-1] == 'neto':
            username += nomes[-2]
        else:
            username += nomes[-1]
        
        base = username
        n = 0

        while username in Usuario.usuarios:
            n += 1
            username = base + str(n)

        return username

    @staticmethod
    def gerar_password():
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '!@#$%&*()/\+-~^}{çÇ'
        return ''.join(random.choice(chars) for _ in range(random.randrange(8,10)))

def menu():
    os.system('clear')
    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    print('XXX                                                XXX')
    print('XXX        1 - Inserir Usuário                     XXX')
    print('XXX        2 - Listar Usuários                     XXX')
    print('XXX        0 - Sair                                XXX')
    print('XXX                                                XXX')
    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    print('')

def criar_usuario(users):
    menu()
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