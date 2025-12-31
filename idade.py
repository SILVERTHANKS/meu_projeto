from datetime import date

nascimento = int(input('Em que Ano que voce nasceu: '))
ano_atual = date.today().year
idade = ano_atual - nascimento

print(f'Você tem {idade} anos em {ano_atual}.')
match idade:

    case i if i <18:

        print(f'Voce é menor de idade  e falta {18 - i } para maior idade')
        print(f'Sua Idade é {idade}')
    case i if  i> 18:
        print(f'Voce e maior de idade {i -18} ')  
        print(f'Sua idade é {idade}') 
