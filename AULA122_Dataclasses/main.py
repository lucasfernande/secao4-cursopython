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
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('Lucas', 'Fernandes', 19)
print(p1.nome_completo)
