radar = int(input('Digite sua velocidade : '))
limite = 80
valor_multar_base = 100
valor_por_km = 7
#mais 7 reais por km execido acima de 80km

if radar > limite:
    execesso = radar - limite
    valor_total = valor_multar_base + execesso*valor_por_km
    print(f'foi multado! Valor da multa: R$ {valor_total:.2f}')
else:
    print('velocidade permitida  poder Continua')    
