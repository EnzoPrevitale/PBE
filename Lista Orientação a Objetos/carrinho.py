from produto import Produto

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, produto):
        if isinstance(produto, Produto):
            self.itens.append(produto)
        else:
            raise TypeError("Produto inválido!")

    def remover(self, produto):
        if isinstance(produto, Produto):
            self.itens.remove(produto)
        else:
            raise TypeError("Produto inválido!")

    def total(self):
        soma = 0
        for item in self.itens:
            soma += item.preco
        return f"R${soma:.2f}"

    def listar_itens(self):
        for item in self.itens:
            str_preco = f"{item.preco:.2f}"
            print(f"{item.nome} | R${str_preco.replace('.', ',')}")