import sqlite3

conexao = sqlite3.connect("banco.db")  # << AGORA TEM EXTENSÃO!
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT NOT NULL,
    saldo REAL NOT NULL,
    cpf TEXT NOT NULL UNIQUE
)
""")
cursor.execute("""
              """)


conexao.commit()
conexao.close()
