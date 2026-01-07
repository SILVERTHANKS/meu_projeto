peso = float(input('Digite seu peso (kg): '))
alt = float(input('Digite sua altura (m): '))

imc = peso / (alt ** 2)

if imc < 18.5:
    print(f'Abaixo do peso | IMC: {imc:.2f}')
elif 18.5 <= imc < 25:
    print(f'Peso normal | IMC: {imc:.2f}')
elif 25 <= imc < 30:
    print(f'Sobrepeso | IMC: {imc:.2f}')
elif 30 <= imc < 35:
    print(f'Obesidade grau I | IMC: {imc:.2f}')
elif 35 <= imc < 40:
    print(f'Obesidade grau II | IMC: {imc:.2f}')
else:
    print(f'Obesidade grau III | IMC: {imc:.2f}')
