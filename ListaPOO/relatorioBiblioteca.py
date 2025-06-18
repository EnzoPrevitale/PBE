from ListaPOO.colecaoLivros import ColecaoLivros
from biblioteca import Biblioteca


class RelatorioBiblioteca:
    def __init__(self, biblioteca:Biblioteca):
        self.biblioteca = biblioteca

    def gerar_relatorio_completo(self):
        itens = self.biblioteca.listar_itens_disponiveis()
        string = "Relatório Completo:\n"
        for i in itens:
            string += self.biblioteca.colecao_itens[i].obter_info()
        return string

    def gerar_relatorio_disponibilidade(self):
        itens = self.biblioteca.listar_itens_disponiveis()
        string = "Relatório de Disponibilidade:\n"
        contador = 0
        for i in itens:
            disponivel = self.biblioteca.colecao_itens[i].disponivel
            if isinstance(self.biblioteca.colecao_itens[i], ColecaoLivros):
                disponivel = self.biblioteca.colecao_itens[i].verificar_disponibilidade_colecao()
            if disponivel:
                string += self.biblioteca.colecao_itens[i].obter_info()
                contador += 1
        string += f"Total de itens disponíveis: {contador}"
        return string

    def gerar_relatorio_emprestimos(self):