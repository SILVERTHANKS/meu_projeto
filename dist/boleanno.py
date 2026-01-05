def poder_dirigir(idade, tem_carteira):
    if idade >= 18 and tem_carteira:
        print('Voce pode Dirigir')
    elif idade < 18:
        falta = 18 - idade
        print(f'Nao poder dirigir Menor de idade faltam {falta} anos') 
    else:
        print('Voce tem idade mais nao tem carteira de motorrista')       
idade= int(input('Digite sua idade '))
carteira = input('Voce tem carteira de motorista (s/n)')
    
tem_carteira = carteira.lower() == 's'
poder_dirigir(idade,tem_carteira)