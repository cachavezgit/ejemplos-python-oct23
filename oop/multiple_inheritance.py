class Rectangulo:
    def _init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo*self.ancho
    
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(largo=lado,ancho=lado)

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

class PiramideTriangular(Cuadrado, Triangulo):
    pass

cuad1 = Cuadrado(20)
triang1 = Triangulo(8,10)

piramide1 = PiramideTriangular(cuad1,triang1)
        