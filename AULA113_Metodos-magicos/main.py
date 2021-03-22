"""
https://rszalski.github.io/magicmethods/

métodos mágicos são métodos que iniciam e terminam com 2 underlines
"""

class A:
    def __new__(cls, *args, **kwargs): # a função new constrói o objeto

        if not hasattr(cls, '_existente'): # exemplo de design pattern, a classe A só vai poder ser instânciada uma vez
            cls._existente = object.__new__(cls)

        return cls._existente

    def __init__(self):
        print('INIT executado')


a = A()
b = A()
print(a == b) # retorna True, a instância B é igual a instância A, pois sempre será instanciada o objeto que já existe

