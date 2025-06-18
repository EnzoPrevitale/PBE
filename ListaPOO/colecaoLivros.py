from itemBiblioteca import ItemBiblioteca


class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, disponivel, itens):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.itens = itens

    def adicionar_livro(self, livro:ItemBiblioteca):
        self.itens.append(livro)

    def verificar_disponibilidade_colecao(self):
        for i in self.itens:
            if not i.disponivel:
                self.disponivel = False
                return False
        return True

    def obter_info(self):
        info = f"Coleção | Título: {self.titulo}\n, Ano: {self.ano_publicacao}, Disponível: {"Sim" if self.verificar_disponibilidade_colecao() else "Não"}:\n"
        for i in self.itens:
            info += f"    {i.obter_info()}\n"
        return info