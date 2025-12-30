class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano =ano
    def discricao_veiculo(self):
        print(f'amarca do carro é {self.marca}')  
        print(f'O ano de fabricacao{self.ano}') 
car1= Carro("toyota",2025)  
car1.discricao_veiculo()       