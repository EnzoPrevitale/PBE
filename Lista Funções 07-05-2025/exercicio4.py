# Dado de 10 faces
def acao_do_jogador(numero_dado):
    if numero_dado % 2 == 0:
        print("Jogador avança")
    else:
        print("Jogador recua")

acao_do_jogador(4)
acao_do_jogador(7)
acao_do_jogador(10)
