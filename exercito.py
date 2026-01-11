from datetime import date
print('Progamar de alistamento'.center(62))
nascimento = int(input('Digite seu ano de nascimento : '))
data_atual = date.today().year
idade = data_atual - nascimento

if idade > 18:
    
    print(f'Voçe e Maior de  idade sua idade e {idade} Fora da idade de alistamento!')
    print(f'Voçe nasceu em {nascimento}')
elif idade == 18:
    print(f'Voce esta na idade de alistamento {idade}')
else:
    print(f'Voce nasceu em {nascimento}')
    print(f'falta {18-idade} anos')     
       