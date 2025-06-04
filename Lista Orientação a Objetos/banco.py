import sqlite3

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect("banco.db")
        self.cursor = self.conexao.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco FLOAT NOT NULL
        )""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        senha TEXT NOT NULL,
        permissao TEXT NOT NULL
        )""")