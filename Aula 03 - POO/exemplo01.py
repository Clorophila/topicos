class Pessoa:
    #setters
    def setNome(self,nome):
        self.nome = nome

    def setIdade(self,idade):
        self.idade = idade

    #getters
    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade
    
    def __str__(self):
        return 'Nome: {}\nIdade: {}'.format(self.nome,self.idade)

welton = Pessoa()

welton.setNome('Welton')
welton.setIdade('34')
print(welton.getNome())
print(welton.getIdade())
print(welton)