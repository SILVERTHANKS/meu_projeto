class Pessoa:
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade

    def saudacao(self):
        print(f"Olá, me chamo {self.nome} e tenho {self.idade} anos.")
p1=Pessoa("carlos", 44) 
p1.saudacao()       