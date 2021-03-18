"""
Exemplo de associação de agregação

Carro e roda

Um carro existe sem a roda, e a roda existe sem o carro

Mas o carro não funciona de forma correta sem a roda, ele PRECISA dela para funcionar corretamente

"""

from classes import CarrinhoDeCompras
from classes import Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Mouse', 79.90)
p2 = Produto('Teclado', 70)
p3 = Produto('Headset', 110.90)
p3

carrinho.insert_produto(p1)
carrinho.insert_produto(p2)
carrinho.insert_produto(p2)

carrinho.listar_produtos()
print(carrinho.soma())

