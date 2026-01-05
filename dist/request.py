import requests

conexao = requests.get('https://www.htx.com/pt-pt/?inviter_id=11350560')
if conexao.status_code == 200:
    print(f'Conexao ativa codigo = ',{conexao.status_code} - {conexao.reason})
else:
    print(f'Conexao nao ativa erro codigo = ',{conexao.status_code} - {conexao.reason})    