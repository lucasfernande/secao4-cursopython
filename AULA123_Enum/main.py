from enum import Enum, auto

"""
enum é utilizado quando há muitas opções de escolha, como por exemplo
as direções que se pode mover um personagem em um jogo
"""


class Directions(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('Cannot move in this direction')

    return f'Moving {direction.name}'


if __name__ == '__main__':
    print(move(Directions.left))
    print(move(Directions.right))
    print(move('back'))
