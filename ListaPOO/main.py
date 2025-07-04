from relatorioBiblioteca import RelatorioBiblioteca
from itemBiblioteca import ItemBiblioteca
from colecaoLivros import ColecaoLivros
from revista import Revista
from biblioteca import Biblioteca

class Main:
    def __init__(self):
        self.livro1 = ItemBiblioteca("aaaaa", 2000, True)
        self.livro2 = ItemBiblioteca("bbbbb", 2001, False)
        self.livro3 = ItemBiblioteca("ccccc", 2002, True)

        self.revista1 = Revista("ppppppp", 2025, True, 5)

        self.colecao1 = ColecaoLivros("Letras", 2025, True, [])

        self.colecao1.adicionar_livro(self.livro1)
        self.colecao1.adicionar_livro(self.livro2)
        self.colecao1.adicionar_livro(self.livro3)

        biblioteca = Biblioteca()
        biblioteca.adicionar_item(self.colecao1)
        biblioteca.adicionar_item(self.livro1)

        relatorio = RelatorioBiblioteca(biblioteca)

        print(relatorio.gerar_relatorio_disponibilidade())

main = Main()
