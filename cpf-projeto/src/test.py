import sqlite3

con = sqlite3.connect("banco.db")
cursor = con.cursor()

cpf = input("Digite o CPF: ")

cursor.execute("SELECT * FROM pessoas WHERE cpf = ?", (cpf,))
pessoa = cursor.fetchone()

if pessoa:
    print("Pessoa encontrada:", pessoa)
else:
    print("CPF não encontrado.")

con.close()
