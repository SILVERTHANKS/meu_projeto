class Carro:
    def __init__(self, ano=None, marca=None, cor=None):
        self.ano =ano
        self.marca=marca
        self.cor=cor
    def informacao(self):
        self.marca = str(input('Digite a amarca do carro : '))
        self.ano = int(input('Digite ano d fabricao :'))
        self.cor = str(input('Digite a cor do seu carro : '))
    def exibir(self):
        print(f'A marca do carro é {self.marca} é um otima marca.')  
        print(f'O ano do seu carro é {self.ano}')
        print(f'A Cor do seu carro é {self.cor}')
meu_carro=Carro()
meu_carro.informacao()   
meu_carro.exibir()               