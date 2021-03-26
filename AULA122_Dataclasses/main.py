"""
Basicamente, dataclasses são syntax sugar para criar classes normais, já com
os métodos alguns métodos incluidos, como __init__, __repr__ e __eq__
"""

from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int


p1 = Pessoa('Lucas', 19)
print(p1)