class Pessoa:
    def __init__(self,nome='',idade=0,profissao=''):
        self.nome=nome
        self.idade=idade
        self.profissao=profissao
        
    def __str__(self):
        return f'{self.nome} tem {self.idade} anos e trabalha como {self.profissao}'
    
    def aniversario(self):
        self.idade +=1
        
    @property
    def saudacao(self):
        if self.profissao:
         return f'Olá, me chamo {self.nome} trabalho de {self.profissao} e tenho {self.idade} anos!'
        else:
            return f'Olá, me chamo {self.nome}!'
    
    
pessoa1 =Pessoa ('Gabriela',25,'Administradora')


print(pessoa1.saudacao)