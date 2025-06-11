from itemBiblioteca import ItemBiblioteca


class Revista(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, disponivel, edicao):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.edicao = edicao

    def atualizar_edicao(self, nova_edicao):
        if nova_edicao > 0:
            self.edicao = nova_edicao
        else:
            raise Exception("O número da edição não pode ser menor ou igual a zero!")

    def restringir_emprestimo(self, dias_max):
        if self.ano_publicacao < 2000:
            if dias_max > 7:
                return False
        return True

    def obter_info(self):
        return f"Título: {self.titulo}, Ano: {self.ano_publicacao}, Disponível: {"Sim" if self.disponivel else "Não"}, Edição: {self.edicao}"