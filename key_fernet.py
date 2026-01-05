from cryptography.fernet import Fernet

key = b'8FhzJ4SO-EhZOI1q8vCxONEskXuSyYukVB6tAffHuNo='
token = b'gAAAAABpPDyMgIMTn5eKjde48CzWxTSH4TyUGD1XcKcVb28bnQxJNooZLHZEWwjEgjj6H2N3pv3LKoi3r1F7VEyHPj7rvg9cYg=='

f = Fernet(key)

try:
    texto = f.decrypt(token).decode()
    print("Texto descriptografado:", texto)
except Exception as e:
    print("Erro ao descriptografar:", e)
