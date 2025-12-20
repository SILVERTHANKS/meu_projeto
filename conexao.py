import requests
conexao = requests.get('https://google.com')
if conexao.status_code == 200:
    print(f'conexao ativa {conexao.status_code}')
else:
    print(f'nao posivel conectar {conexao.status_code} ')    