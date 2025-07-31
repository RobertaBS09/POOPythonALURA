class Carro:
    carros=[]
    def __init__(self, modelo='',cor='',ano=0):
        self.modelo=modelo
        self.cor=cor
        self.ano=ano
        self.ativo = False
        Carro.carros.append(self)
    def __str__(self):
        return f'Modelo: {self.modelo} - Cor: {self.cor} - Ano: {self.ano}'
    
    def listar_carros():
        for carro in Carro.carros:
            print(f'Modelo: {carro.modelo} - Ano: {carro.cor} -Cor: {carro.ano} -Ativo: {carro.ativo}')
    
        
carro1=Carro('Camaro','Preto',2020)
carro2=Carro('Urus','Roxo',2021)

Carro.listar_carros()
        