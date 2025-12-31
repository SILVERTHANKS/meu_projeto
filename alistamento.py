from datetime import date
try:
    ano_atual = date.today().year
    ano_nascimento = int(input('Digite ano do seu nascimento : '))
    ano = ano_atual - ano_nascimento
    data_alistamento = ano_nascimento + 18
    if ano == 18:
        print(f'idade permitida voce poder se alistar voce tem {ano} anos!')
    elif ano < 18 :
        falta_ano = 18 - ano
        print(f'voce é menor de idade voce tem {ano} anos ,Faltam {falta_ano}  ano! ')

    elif ano > 18 :
        fora_idade = ano - 18
        print(f'Passou da idade de alistameto militar sua idade {ano} anos e passaram {fora_idade} anos ! ')
except ValueError:
    
 print('erro:voce digitou um número invalido')
