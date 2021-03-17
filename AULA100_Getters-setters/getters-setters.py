class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * percentual / 100)
        return self.preco

    @property
    def preco(self): # getter - busca
        return self._preco

    @preco.setter
    def preco(self, preco): # setter - seta, configura
        if isinstance(preco, str):
            preco = float(preco.replace('R$', ''))

        self._preco = preco


prod = Produto('Camiseta', 159.90)
print(prod.desconto(10))

prod2 = Produto('Caneca', 'R$15')
print(prod2.desconto(10))

