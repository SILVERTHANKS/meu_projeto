from validate_docbr import CPF
cpf = CPF()
ni = input('Digite seu cpf')
if cpf.validate(ni):
    print(f'SEU CPF E VALIDO',{ni})
else:
    print(f'O CPF E INVALIDO: ')    