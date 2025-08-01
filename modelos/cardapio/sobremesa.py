class Sobremesa:
    def __init__(self,nome,preco,tipo,tamanho,descricao):
        super().__innit__(nome,preco)
        self.tipo = tipo
        self.tamanho = tamanho
        self.descricao = descricao
    def __str__(self):
        return f'Sobremesa: {self.tipo}| Tamanho: {self.tamanho} | Descrição: {self.descricao}'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.10)