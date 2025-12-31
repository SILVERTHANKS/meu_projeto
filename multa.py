velocidade = int(input('Diigite sua velocidade : '))
vel_max = 80
multa_fixa = 100
multa_por_km = 10
if velocidade > vel_max:
    excesso = velocidade - vel_max
    multa = multa_fixa + (excesso * multa_por_km)
    print(f'Você passou do limite! Excedeu {excesso} km/h.')
    print(f'Sua multa é de R$ {multa}.')
else:
    print(f'limite permitido sua velocidade é de {velocidade}')    