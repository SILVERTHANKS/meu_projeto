from random import randint
print('jogo adivinhacao'.center(50))
print('ola tenta adivinha que numero estou pensado')
computador = randint(1, 10)
tentativa = 0
acertou = False
while not acertou:
    tentativa+=1
    jogador = int(input('Digite um número : '))
    
    if jogador == computador:
        
        acertou = True
        print(f'Você acertou! O número era {computador}.')
        print(f'Você jogou {tentativa} vez(es).')
    else:
        dica = "maior" if jogador < computador else "menor"
        print(f'Você errou... O número é {dica} que {jogador}.')
        print('Tente novamente...') 
           
