print('Bem Vindo ao Caixa'.center(50))

saldo = 1000
senha_correta = '1234'
while True:
    senha = input('Digite sua senha : ')
    if senha_correta == senha :
            print('senha correta!Acesso liberado.')
    
            break
    else:
        print('Senha errada,tente novamente.\n')    

            
while True:    
        print('\nDigite opcoes')
        print('opcao [1]- verifica saldo')
        print('opcao [2] - Depositar')
        print('opcao [3] Saque de valor')
        print('opcao [4] Sair')
        
        opcao = input('Escolha uma opcao : ')
        if opcao == '1':
            print(f'seu saldo é {saldo:.2f}')  
        
        elif opcao == '2':
            valor = float(input('Digite o valor para deposito :'))
            saldo+= valor
            print(f'Deposito realizado com sucesso!Seu Novo saldo é {saldo:.2f}') 
        elif opcao == '3':
            valor = float(input('Digite o valor :'))
            if valor <= saldo:
                saldo-= valor
                print(f'O valor sacado foi {valor:.2f} e seu novo saldo é {saldo:.2f}')
            
            else:
                print('saldo insuficiente')
        elif opcao == '4':
            print('Saindo do Progama ...')
            break
        else:
            print('Opcao invalida,escolher opcao [4]')
print('FIM')                
                         