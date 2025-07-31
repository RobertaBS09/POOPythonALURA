from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça','Gourmet')
restaurante_praca.receber_avaliacao('Roberta',10)
restaurante_praca.receber_avaliacao('Ronaldo',8)
restaurante_praca.receber_avaliacao('Selma',2)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
    