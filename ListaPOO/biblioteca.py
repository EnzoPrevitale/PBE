from itemBiblioteca import ItemBiblioteca


class Biblioteca:
    def __init__(self):
        self.colecao_itens = {}

    def adicionar_item(self, item:ItemBiblioteca):
        self.colecao_itens[item.titulo] = item

    def remover_item(self, item:ItemBiblioteca):
        self.colecao_itens.pop(item.titulo)

    def listar_itens_disponiveis(self):
        lista = []
        for titulo in self.colecao_itens:
            lista.append(titulo)
        return lista

    def contar_itens_emprestados(self):
        num = 0
        for item in self.colecao_itens:
            if not self.colecao_itens[item].disponivel:
                num += 1
        return num
