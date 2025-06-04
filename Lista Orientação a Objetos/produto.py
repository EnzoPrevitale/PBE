class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco

    def __str__(self):
        return f"{self.nome} - R${self.__preco:.2f}"

    def exibir_dados(self):
        print(self)

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("O valor não pode ser negativo!")
        self.__preco = valor
