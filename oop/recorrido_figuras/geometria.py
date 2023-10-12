class Circulo:
    pass

class Cuadrado:
    pass

class Triangulo:
    base = 0
    altura = 0

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcula_area(self):
        return (self.base*self.altura)/2
