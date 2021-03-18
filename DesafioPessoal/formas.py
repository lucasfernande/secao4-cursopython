class Forma:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        pass

class Retangulo(Forma):
    def calcular_area(self):
        area = self.base * self.altura
        return area

class Triangulo(Forma):
    def calcular_area(self):
        area = self.base * self.altura / 2
        return area

class Quadrado(Forma):
    def calcular_area(self):
        area = self.base ** 2
        return area

class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.pi = 3.14

    def calcular_area(self):
        area = self.pi * self.raio ** 2
        return area
