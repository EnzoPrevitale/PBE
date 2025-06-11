class ItemBiblioteca:
    def __init__(self, titulo, ano_publicacao, disponivel):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"{self} foi emprestado.")
        else:
            raise Exception("Livro já emprestado!")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"{self} foi devolvido.")
        else:
            raise Exception("Livro já disponível!")

    def obter_info(self):
        return f"Título: {self.titulo}, Ano: {self.ano_publicacao}, Disponível: {"Sim" if self.disponivel else "Não"}"