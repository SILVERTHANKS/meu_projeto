class Cadastro:
    def __init__(self):
        self.nomes = []
        self.telefones = []
    def entrada_de_clientes(self):
        while True:      
               
            nome=input('Digite o nome do cliente : ').strip() 
            telefone= input('Digite o seu telefone :')
            self.nomes.append(nome)
            self.telefones.append(telefone)
            
            opcao =input('Digite (c/n) c para continuar e "s" para sair ').lower()
            
            if opcao == "s":
                break
                
        print("\nClientes Cadastrado:".center(32))
        for i in range(len(self.nomes)):
            print(f'Nome : {self.nomes[i]}| telefone:{self.telefones[i]}')            
cadastro1=Cadastro()
cadastro1.entrada_de_clientes()        