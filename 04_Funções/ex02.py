'''
Exercício 2
- Elabore uma aplicação capaz de gerar o currículo de
uma pessoa em HTML.
- Os parâmetros para o currículo são: nome, endereço,
telefone, e-mail, escolaridade e experiência
profissional.
- Você pode utilizar as tags HTML da sua preferência.
- Utilize funções para organizar o código fonte da
aplicação.
'''
import os.path
import re

def get_endereco():
    rua = input('Digite seu endereço (logradouro): ')
    while(True):
        try:
            entrada = input('Digite um número: ')
            if not entrada.isdigit():
                raise ValueError
            else:
                numero = int(entrada)
            break
        except ValueError:
            print('Valor inválido. Por favor digite um número inteiro.')
    complemento = input('Digite o complemento do endereço: ')
    bairro = input('Digite seu bairro: ')
    cidade = input('Digite sua cidade: ')
    estado = input('Digite seu estado: ')
    pais = input('Digite seu pais: ')
    endereco = {
                'rua':rua,
                'numero':numero,
                'complemento':complemento,
                'bairro':bairro,
                'cidade':cidade,
                'estado':estado,
                'pais':pais,
    }
    return endereco

def get_telefone():
    tel = input('Digite seu telefone: ')
    '''
    if tel.isdigit():
        tel.insert(0,'(')
        tel.insert(3,')')
        tel.insert(-5,'-')
    '''
    return tel

def get_email():
    while(True):
        try:
            mail = input('Digite seu e-mail: ')
            if not re.search(r'[\w.-]+@[\w.-]+.\w+', mail):
                raise ValueError
            else:
                break
        except ValueError:
            print('Valor inválido. Por favor digite um e-mail válido.')
    return mail

def get_escolaridade():
    continuar = True
    escolaridade = []
    while(continuar):
        grau = input('Digite seu grau de formação: ')
        instituicao = input('Digite o nome da instituição onde obteve essa formação: ')

        escolaridade.append({
            'grau':grau,
            'instituicao':instituicao,
        })

        while(True):
            try:
                opcao = input('Deseja adicionar mais itens da sua formação? (s/n): ').lower()
                if(opcao=='n'):
                    continuar=False
                elif(opcao=='s'):
                    pass
                else:
                    raise ValueError
                break
            except ValueError:
                print('Valor inválido.')
    
    return escolaridade

def get_experiencia():
    continuar = True
    experiencia = []
    while(continuar):
        cargo = input('Digite o cargo no qual trabalhou: ')
        empresa = input('Digite o nome da empresa onde exerceu esse cargo: ')
        periodo = input('Digite o período em que trabalhou nessa empresa: ')

        experiencia.append({
            'cargo':cargo,
            'empresa':empresa,
            'periodo':periodo,
        })

        while(True):
            try:
                opcao = input('Deseja adicionar mais itens na sua exeperiência? (s/n): ').lower()
                if(opcao=='n'):
                    continuar=False
                elif(opcao=='s'):
                    pass
                else:
                    raise ValueError
                break
            except ValueError:
                print('Valor inválido.')
    
    return experiencia

def gerar_html(nome,endereco,telefone,email,escolaridade,experiencia):
    html = [
            '<DOCTYPE! html>\n',
            '<html lang="pt-br">\n',
            '<head>\n',
            '  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n',
            '  <title>Currículo - {}</title>\n'.format(nome),
            '</head>\n',
            '<body class="curriculo">\n',
            '  <header>\n',
            '    <h1>{}</h1>\n'.format(nome),
            '  </header>\n',
            '  <nome>\n',
            '    {}\n'.format(nome),
            '  </nome>\n',
            '  <endereco>\n',
            '    Endereço:\n',
            '    <rua>{}</rua>, <numero>{}</numero>. <complemento>{}</complemento>\n'.format(endereco['rua'],endereco['numero'],endereco['complemento']),
            '    Bairro: {}\n'.format(endereco['bairro']),
            '    <cidade>{}</cidade> - <estado>{}</estado>, <pais>{}</pais>.\n'.format(endereco['cidade'],endereco['estado'],endereco['pais']),
            '  </endereco>\n',
            '  <telefone>\n',
            '    Telefone: {}\n'.format(telefone),
            '  </telefone>\n',
            '  <email>\n',
            '    E-mail: {}\n'.format(email),
            '  </email>\n',
    ]

    for item in escolaridade:
        html.extend([
            '  <escolaridade>\n',
            '    <grau>{}</grau>\n'.format(item['grau']),
            '    <instituicao>{}</instituicao>\n'.format(item['instituicao']),
            '  </escolaridade>\n',
        ])

    for item in experiencia:
        html.extend([
            '  <experiencia>\n',
            '    <cargo>{}</cargo>\n'.format(item['cargo']),
            '    <empresa>{}</empresa>\n'.format(item['empresa']),
            '    <periodo>{}</periodo>\n'.format(item['periodo']),
            '  </experiencia>\n',
        ])

    html.extend([
            '  <footer>\n',
            '    Gerado automaticamente em linguagem Python.\n',
            '  </footer>\n',
            '</body>\n',
            '</html>\n',
    ])
    return html

def gravar_html(html):
    caminho = 'curriculo.html'
    n = 0
    while(True):
        if os.path.exists(caminho):
            n += 1
            caminho = 'curriculo({}).html'.format(n)
        else:
            break

    file = open(caminho,'w')
    file.writelines(html)
    file.close()

    if os.path.exists(caminho):
        print('Arquivo "{}" gerado com sucesso!'.format(caminho))
    else:
        print('Falha ao gerar o arquivo.')

nome = input('Digite seu nome completo: ')
endereco = get_endereco()
telefone = get_telefone()
email = get_email()
escolaridade = get_escolaridade()
experiencia = get_experiencia()

print(nome)
print(endereco)
print(telefone)
print(email)
print(escolaridade)
print(experiencia)

html = gerar_html(nome,endereco,telefone,email,escolaridade,experiencia)

gravar_html(html)