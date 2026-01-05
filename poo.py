class Note:
    def __init__(self, marca, configuracao, memoria ):
        self.marca = marca
        self.configuracao = configuracao
        self.memoria = memoria
    def Ligar(self):
        print('Ligando o Notebook')
        
    def Desligando(self):
        print('Desligando ...')   
    def Info(self):
        print(f'Marca: {self.marca}')
        print(f'Configuracao: {self.configuracao}')
        print(f'Memória : {self.memoria}')     
        

note1 = Note(marca="Asus", configuracao="i7", memoria="16GB")

note1.Ligar()
print(note1.marca)
print(note1.configuracao)
print(note1.memoria)
note1.Desligando()

        
        