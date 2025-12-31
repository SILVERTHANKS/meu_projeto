from datetime import date
try:
 ano_atual = date.today().year
 ano_nasc = int(input('Digite seu ano de nascimento :'))
 ano = ano_atual - ano_nasc
 if ano == 18:
  print(f'Voce tem {ano} anos é permiitido alistamento   ')
 
 elif ano > 18:
  pass_idade = ano - 18
  print(f'voce passou da idade {ano} passou {pass_idade} anos ')

 elif ano < 18:
  menor_idade = 18 - ano
  print(f'Menor de idade {ano} anos,falta anos {menor_idade}') 
except ValueError:
  print('Essa opcao nao e validade tente novamente .')