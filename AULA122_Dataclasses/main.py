"""
Basicamente, dataclasses são syntax sugar para criar classes normais, já com
os métodos alguns métodos incluidos, como __init__, __repr__ e __eq__
"""

from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int

    def __post_init__(self):  # o __post_init é executado depois do init
        if not isinstance(self.nome, str):
            raise TypeError(f'Tipo inválido {type(self.nome).__name__} != str in {self}')

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('Lucas', 'Fernandes', 19)
p2 = Pessoa(123, 'Maria', 25)
