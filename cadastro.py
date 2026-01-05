nomes = []
idades = []
senhas = []
while True:
    nome = (input('Digite seu Nome : ')).lower()
    idade = int(input('Digite sua idade : '))
    senha = (input('Digite sua senha aqui : ')).lower()
    nomes.append(nome)
    idades.append(idade)
    senhas.append(senha)
    print("Cadastro realizado!")
    print("Nomes:", nomes)
    print("Idades:", idades)
    print("Senhas:", senhas)
    continuar = input('Deseja continuar ? (s/n)').lower()
    if continuar == 'n':
        break
print('Fim')