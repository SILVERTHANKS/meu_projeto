print('\33[36m*Fibonacci Matematica*\33[36m'.center(50))
n1 = int(input('Digite sua sequencia aqui : '))
t1 = 0
t2 = 1
cont = 2
print(f'→ {t1} → {t2}',end ='')
while cont < n1:
    
    t3 = t1 + t2
    print(f'→ {t3}',end='')
    t1 = t2
    t2 = t3
    cont+=1    
print('Fim')   
