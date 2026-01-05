from datetime import date
nascimento = int(input('Digite sua data de nascimento : '))
ano_atual = date.today().year
idade =ano_atual - nascimento
if idade == 18:
    print(f'Voce tem {idade} idade para alistamento')
elif idade < 18:
    falta = 18 - idade
    print(f'Voce é menor de idade, voce tem {idade}anos')
    print(f'Faltam {falta} ano para seu alistamento...')
        
else:
    if idade > 18:
        passaram = idade - 18
        print(f'Voce passou do ano de alistamento sua idade é {idade}')
        print(f'Passaram {passaram} anos')        
