from produto import Produto
from usuario import Usuario
from carrinho import Carrinho
from banco import Banco
import sqlite3
import pandas as pd
import hashlib

def encrypt(text):
    hash_obj = hashlib.sha256()
    hash_obj.update(text.encode('utf-8'))
    encrypted_text = hash_obj.hexdigest()

    return encrypted_text

def login(nome, senha):
    if nome in list(usuarios["nome"]):
        senha = encrypt(senha)
        while senha != senha == usuarios[usuarios['nome'] == nome]["senha"]:
            senha = encrypt(input("Senha incorreta! Tente novamente: "))
        else:
            return True
    else:
        print("Usuário não encontrado!")
        return False

banco = Banco()

carrinho = Carrinho()

while True:
    usuarios = pd.read_sql("SELECT * FROM usuarios", banco.conexao)
    produtos = pd.read_sql("SELECT * FROM produtos", banco.conexao)
    print("[1] - Fazer Login | [2] - Fazer cadastro | [3] - Sair")
    opcao = int(input("Escolha: "))
    if opcao == 1:
        nome_usuario = input("Digite o seu nome: ")
        senha_usuario = input("Digite a sua senha: ")
        if login(nome_usuario, senha_usuario):
            usuario = Usuario(nome_usuario, usuarios[usuarios['nome'] == nome_usuario]["permissao"])
    elif opcao == 2:
        nome_usuario = input("Digite o seu nome: ")
        senha_usuario = encrypt(input("Digite a sua senha: "))
        banco.cursor.execute(f"""INSERT INTO usuarios (nome, senha, permissao) VALUES ('{nome_usuario}', '{senha_usuario}', 'cliente')""")
    break

banco.conexao.commit()