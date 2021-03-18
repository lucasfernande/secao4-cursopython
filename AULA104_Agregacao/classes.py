class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def insert_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for prod in self.produtos:
            print(prod.nome, prod.valor)

    def soma(self):
        total = 0
        for prod in self.produtos:
            total += prod.valor

        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
