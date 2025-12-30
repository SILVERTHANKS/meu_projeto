from cryptography.fernet import Fernet
chave_secreta = Fernet.generate_key()
fernet = Fernet(chave_secreta)
#criar funcao
def criptografia(senha):
    return fernet.encrypt(senha.encode()).decode()

def descriptografar(senha_criptografia):
    return fernet.decrypt(senha_criptografia.encode()).decode()

senha_original = 'Carlos'
senha_criptografada = criptografia(senha_original)
senha_descriptografada = descriptografar(senha_criptografada)
print(f'Senha Original : {senha_original}')
print(f'Senha Criptografada : {senha_criptografada}')
print(f'Senha Descriptografada : {senha_descriptografada}')
print(f'A chave secreta é : {chave_secreta}')