n1 = int(input('Digite um numero '))
#Lê um texto do usuário e converte para inteiro, guardando em n1.
primo = True
#Começa assumindo que o número é primo. Esse é o seu “sinalizador” booleano.
if n1 < 2:
    primo = False
#Números menores que 2 não são primos, então já marcamos o estado como falso.    
else:
#Só entramos aqui se n1 for 2 ou maior.    
    for i in range(2, n1):
#Tenta todos os possíveis divisores i entre 2 e n1-1. Se algum dividir exatamente, então n1 não é primo.        
        if n1 % i == 0:
 #O operador % (módulo) dá o resto da divisão. Se o resto for 0, significa que i é divisor de n1.
#Atualiza o estado: primo vira False.          
            primo = False
            break
if primo:
    print(f'O Número é primo {n1}')
    
else:
    print(f'O número não é primo {n1}')            