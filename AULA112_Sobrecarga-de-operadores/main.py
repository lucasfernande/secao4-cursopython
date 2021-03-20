"""
Sobrecarga de operadores é definido por métodos especiais
Altera o comportamento de operadores com classes definidos pelo usuário

"""


class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def __repr__(self):  # mudando o comportamento do print da classe
        return f"<class Retangulo({self.x}, {self.y})>"

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    def __lt__(self, other):  # o metodo lt é igual ao < (menor que)
        area1 = self.get_area()
        area2 = other.get_area()

        if area1 < area2:
            return True

        return False

    def __gt__(self, other):  # o metodo gt é igual ao > (maior que)
        area1 = self.get_area()
        area2 = other.get_area()

        if area1 > area2:
            return True

        return False


r1 = Retangulo(2, 5)
r2 = Retangulo(7, 3)
r3 = r1 + r2
print(r3)

print(r1 > r2)
print(r2 < r3)
