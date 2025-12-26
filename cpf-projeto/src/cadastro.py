import sqlite3

# Conectar ao banco
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

print("=== CADASTRAR NOVA PESSOA ===")

nome = input("Digite o nome: ")
cpf = input("Digite o CPF: ")
saldo = float(input("Digite o saldo: "))

try:
    cursor.execute("""
        INSERT INTO pessoas (nome, cpf, saldo)
        VALUES (?, ?, ?)
    """, (nome, cpf, saldo))

    conexao.commit()
    print("\n✔ Pessoa cadastrada com sucesso!")

except sqlite3.IntegrityError:
    print("\n❌ ERRO: CPF já existe no banco!")

conexao.close()
